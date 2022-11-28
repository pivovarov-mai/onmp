from django.utils import timezone
from django.db import models

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, first_name, last_name, **extra_fields):
        '''
        Create and save a user with the given email, and password.
        '''
        if not email:
            raise ValueError('Почта должна быть установлена')
        if not password:
            raise ValueError('Пароль должен быть установлен')
        if not first_name:
            raise ValueError('Имя должно быть установлено')
        if not last_name:
            raise ValueError('Фамилия должна быть установлена')

        user = self.model(email=self.normalize_email(email),
                          first_name=first_name,
                          last_name=last_name,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, first_name,
                    last_name, **extra_fields):
        extra_fields.setdefault('is_admin', False)
        return self._create_user(email, password, first_name,
                                 last_name, **extra_fields)

    def create_superuser(self, email, password, first_name='admin',
                         last_name='admin', **extra_fields):
        extra_fields.setdefault('is_admin', True)

        if extra_fields.get('is_admin') is not True:
            raise ValueError(
                'Суперпользователь должен иметь is_admin=True.'
            )

        return self._create_user(email, password, first_name,
                                 last_name, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        'Email почта',
        unique=True,
        max_length=255,
        blank=False,
    )
    first_name = models.CharField(
        'Имя',
        max_length=50,
        blank=False,
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=50,
        blank=False,
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
        default=timezone.now,
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

    @property
    def is_staff(self):
        "Is the user an admin?"
        return self.is_admin

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
