import uuid

from django.db import models
from django.db.models.signals import pre_delete
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import (
    BaseUserManager,
    AbstractBaseUser,
)
from django.core.mail import send_mail
from django.conf import settings
from django.dispatch import receiver

from celery import shared_task

from .utils import (
    generate_msg_confirm_account_creation,
    generate_msg_reset_password,
    generate_msg_reseted_password,
)

from .user_profile_funcs import (
    user_profile_delete,
)


@shared_task()
def celery_send_mail(theme: str, emails: list[str], msg: str):
    return send_mail(
        theme,
        'Сообщение',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=emails,
        fail_silently=True,
        html_message=msg
    )


def async_or_sync_sending_message(theme: str, emails: list[str], msg: str):
    try:
        celery_send_mail.delay(theme, emails, msg)
    except Exception:
        celery_send_mail(theme, emails, msg)


class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email,
                     password, **extra_fields):
        '''
        Create and save a user with the given email, and password.
        '''
        if not email:
            raise ValueError('Почта должна быть установлена')
        if not password:
            raise ValueError('Пароль должен быть установлен')

        extra_fields.setdefault('is_superuser', False)

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        if settings.EMAIL_HOST_PASSWORD != '' and user.is_admin is False:
            async_or_sync_sending_message(
                'onmp подтверждение аккаунта',
                [user.email],
                generate_msg_confirm_account_creation(user.email_id)
            )
        else:
            user.email_confirmed = True
            user.save()
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_admin', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_email_confirmed', True)

        if extra_fields.get('is_admin') is not True:
            raise ValueError(
                'Суперпользователь должен иметь is_admin=True.'
            )

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    '''
    Overriden user model for medical and secure purposes
    '''

    email = models.EmailField(
        'Email почта',
        unique=True,
        max_length=255,
        blank=False,
    )
    email_id = models.UUIDField(
        'Индекс почты для подтверждения',
        unique=True,
        blank=True,
        default=uuid.uuid4,
        editable=False,
    )
    is_email_confirmed = models.BooleanField(
        'Подтвержден ли email',
        default=False,
    )
    is_admin = models.BooleanField(
        'Администратор',
        default=False,
        help_text='Является ли пользователь администратором сайта'
    )
    is_active = models.BooleanField(
        'Активен ли',
        default=True,
        help_text='Используется вместо удаления аккаунта',
    )
    date_joined = models.DateTimeField(
        'Дата создания аккаунта',
        auto_now_add=True,
        blank=True,
    )

    # TODO: Добавить пару полей

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def reset_password_send(self):
        self.email_id = uuid.uuid4()
        self.save()
        celery_send_mail.delay('Сброс пароля', [self.email],
                               generate_msg_reset_password(self.email_id))

    def reseted_password_send(self, password):
        celery_send_mail.delay('Новый пароль', [self.email],
                               generate_msg_reseted_password(password))

    @property
    def is_staff(self):
        "Is the user an admin?"
        return self.is_admin

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'


@receiver(pre_delete, sender=User)
def delete_profiler(sender, instance, using, **kwargs):
    user_profile_delete({'account_user_id': instance.pk})
