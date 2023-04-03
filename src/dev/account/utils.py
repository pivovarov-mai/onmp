def generate_msg(uuid: str):
    return f'Чтобы подтвердить аккаунт перейдите по <a href="http://localhost:8000/api/v1/account/email_confirm/{uuid}">Ссылке</a>'
    