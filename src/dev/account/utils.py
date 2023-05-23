from django.conf import settings
from django.urls import reverse


def generate_msg_confirm_account_creation(uuid: str):
    return f'Чтобы подтвердить аккаунт перейдите по <a href="{settings.DOMEN}{reverse("email_confirm", args=[uuid])}">Ссылке</a>'


def generate_msg_reset_password(uuid: str):
    return f'Чтобы очистить пароль перейдите по <a href="{settings.DOMEN}{reverse("new_password_send", args=[uuid])}">Ссылке</a>'


def generate_msg_reseted_password(password: str):
    return f'Ваш новый пароль от сайта onmp - {password}. Рекомендуем сменить пароль в настройках пользователя на более сложный.'
