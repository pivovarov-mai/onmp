from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import (
    LoginView,              # Low level
    # RegisterView,           # Low level

    UserGetTokenAPI,
    UserCreateAPI,
    GetProfileAPI,
    CheckEmailAPI,
    SetNewPasswordAPI,
    ResetPasswordSendMail,
    ResetPasswordConfirmation,
    RetrySendMail,
)


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('token/', UserGetTokenAPI.as_view(), name='token'),
    path('user_create/', UserCreateAPI.as_view(), name='user_create'),
    path('resend_mail/', RetrySendMail.as_view(), name='resend_mail'),
    path('user_profile/', GetProfileAPI.as_view(), name='user_profile'),
    path('email_confirm/<uuid:id>',
         CheckEmailAPI.as_view(),
         name='email_confirm'),
    path('reset_pass_send_mail/',
         ResetPasswordSendMail.as_view(),
         name='res_new_password_send_req'),
    path('reset_pass_confirmation/<uuid:email_id>/',
         ResetPasswordConfirmation.as_view(),
         name='res_new_password_send'),
    path('set_new_password/',
         SetNewPasswordAPI.as_view(),
         name='set_new_password'),
]
