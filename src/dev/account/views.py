from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
from django.urls import reverse
from django.views import View
from django.contrib.auth import (
    authenticate,
    login,
    logout,
    get_user_model,
)
from django.contrib.auth.password_validation import validate_password

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import (
    TokenAuthentication,
)
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
    AllowAny,
)

from drf_yasg.utils import swagger_auto_schema

from .forms import UserLoginForm, UserRegisterForm

from .serializers import (
    UserSerializerCreate,
    UserSerializerMaximum,
)

from .models import async_or_sync_sending_message, User

from .utils import generate_msg_confirm_account_creation

from config.loggers_conf import slog

from .user_profile_funcs import (
    user_profile_retrieve,
    user_profile_update,
    user_profile_create,
    user_profile_show,
)

from .swagger import (
    SW_GET_TOKEN,
    SW_CREATE_USER,
    SW_GET_PROFILE,
    SW_SET_PASSWORD,
    SW_RESET_PASSWORD_CONFIRMATION,
    SW_RESET_PASSWORD_REQUEST,
    SW_RESEND_MAIL,
    SW_SHOW_ALL_PROFILES,
    SW_UPDATE_PROFILE,
)


class UserGetTokenAPI(APIView):
    '''
    Api for getting token by user fields in POST method or by session auth
    '''
    permission_classes = [AllowAny]

    @swagger_auto_schema(**SW_GET_TOKEN)
    def post(self, request):
        if request.user.is_anonymous:
            user = authenticate(request,
                                username=request.data.get('email', ''),
                                password=request.data.get('password', ''))
        else:
            user = request.user

        if user:
            if not user.is_email_confirmed:
                return Response({'error': 'Подтвердите email'},
                                status=status.HTTP_401_UNAUTHORIZED)
            return Response({
                'token': Token.objects.get_or_create(user=user)[0].key})
        return Response({
            'error': 'Данные пользователя неверны, либо вы не авторизованны'},
                        status=status.HTTP_401_UNAUTHORIZED)


class UserCreateAPI(APIView):
    '''
    Creates new user account
    '''

    @swagger_auto_schema(**SW_CREATE_USER)
    def post(self, request):
        user_ser = UserSerializerCreate(data=request.data)
        if user_ser.is_valid(raise_exception=True):
            # Checker for user profile
            if 'first_name' not in request.data or \
                    'middle_name' not in request.data or \
                    'last_name' not in request.data:
                return Response(
                    'Какой-то параметр ФИО отсутствует',
                    status=status.HTTP_418_IM_A_TEAPOT
                )

            created_user = get_user_model().objects.create_user(
                user_ser.validated_data['email'],
                user_ser.validated_data['password'])

            slog('Создан профиль с id: ' + str(
                    user_profile_create({
                        'account_user_id': created_user.pk,
                        **request.data
                    })[0]['id']
                )
            )
            return Response({'success'}, status=status.HTTP_201_CREATED)
        return Response(user_ser.errors, status=status.HTTP_418_IM_A_TEAPOT)


class GetProfileAPI(APIView):
    '''
    Get profile data for user by token
    '''
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(**SW_GET_PROFILE)
    def get(self, request):
        user_profile = user_profile_retrieve({
            'account_user_id': request.user.pk
        })[0]
        return Response({
                'user': UserSerializerMaximum(instance=request.user).data,
                'profile': user_profile
            }
        )


class ProfileDataUpdateAPI(APIView):
    '''
    Update user's profile data.
    Required Token.
    '''
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(**SW_UPDATE_PROFILE)
    def get(self, request):
        return Response(
            user_profile_update({
                'account_user_id': request.user.pk,
                **request.GET.dict(),
            })
        )


class ShowAllProfilesAPI(APIView):
    '''
    Show all profiles.
    Required admin permission.
    '''
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(**SW_SHOW_ALL_PROFILES)
    def get(self, request):
        return Response(user_profile_show())


class CheckEmailAPI(APIView):
    '''
    Checks uuid and if it will be found then is_email_confirmed sets to True
    '''

    @swagger_auto_schema(
        responses={
            '200': 'Email подтвержден',
            '401': 'Пользователь не существует'
        }
    )
    def get(self, request, id):
        user = get_user_model().objects.filter(email_id=id)
        if user.exists():
            user = user.first()
            user.is_email_confirmed = True
            user.save()
            return Response({'success'})
        return Response({'error': 'Пользователь не существует'},
                        status=status.HTTP_401_UNAUTHORIZED)


class RetrySendMail(APIView):
    '''
    View to sending mail again for any purposes
    '''

    @swagger_auto_schema(**SW_RESEND_MAIL)
    def post(self, request):
        if 'email' not in request.data:
            return Response({'error': 'Введенные данные не верны'},
                            status=status.HTTP_401_UNAUTHORIZED)

        email = request.data['email']
        user = User.objects.filter(email=email)
        if not user.exists():
            return Response({'error': 'Пользователь не существует'},
                            status=status.HTTP_404_NOT_FOUND)

        async_or_sync_sending_message(
            'onmp подтверждение аккаунта',
            [email],
            generate_msg_confirm_account_creation(user[0].email_id))
        return Response(
            'Повторное сообщение отправлено, придет в ближайшее время'
        )


class SetNewPasswordAPI(APIView):
    '''
    Sets new password if the old one was been accepted
    '''
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(**SW_SET_PASSWORD)
    def post(self, request):
        if 'new_password' not in request.data:
            return Response({'error': 'Пароль необходим'},
                            status=status.HTTP_401_UNAUTHORIZED)
        new_pass = request.data['new_password']
        if request.user.check_password(new_pass):
            return Response({'error': 'Требуется другой пароль'},
                            status=status.HTTP_418_IM_A_TEAPOT)
        try:
            validate_password(new_pass)
            request.user.set_password(new_pass)
            request.user.save()
            logout(request)
            return Response({'success'})
        except Exception:
            return Response({'error': 'Требуется более сильный пароль'},
                            status=status.HTTP_418_IM_A_TEAPOT)


class ResetPasswordSendMail(APIView):
    '''
    Send mail to confirm reset password
    '''

    @swagger_auto_schema(**SW_RESET_PASSWORD_REQUEST)
    def get(self, request):
        if 'email' not in request.GET:
            return Response({'error': 'Email необходим'},
                            status=status.HTTP_418_IM_A_TEAPOT)

        users = get_user_model().objects.filter(
            email=request.GET['email']
        )
        if not users.exists():
            return Response({'error': 'Email не существует'},
                            status=status.HTTP_401_UNAUTHORIZED)

        users.first().reset_password_send()
        return Response({'success'})


class ResetPasswordConfirmation(APIView):
    '''
    Reset password confirmation if email_id is true
    generate new password and then send to email
    '''

    @swagger_auto_schema(**SW_RESET_PASSWORD_CONFIRMATION)
    def get(self, request, email_id):
        user = get_object_or_404(get_user_model(), email_id=email_id)
        password = get_user_model().objects.make_random_password()
        user.set_password(password)
        user.reseted_password_send(password)
        user.save()
        return Response({'success'})


class LoginView(View):
    '''Login low-level CBV'''
    def get(self, request, *args, **kwargs):
        return render(request, 'account/login.html', {
            'form': UserLoginForm,
        })

    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            get_user = authenticate(username=form.cleaned_data['email'],
                                    password=form.cleaned_data['password'])
            if get_user is None:
                form.errors['email'] = ['Данные введены неверно']
            else:
                login(request, get_user)
                return redirect(reverse('home'))
        return render(request, 'account/login.html', {
            'form': form,
        })


class RegisterView(View):
    '''Signup low-level CBV'''
    def get(self, request, *args, **kwargs):
        return render(request, 'account/signup.html', {
            'form': UserRegisterForm,
        })

    def post(self, request, *args, **kwargs):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            get_user_model().objects.create_user(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
            )
            return redirect(reverse('home'))
        return render(request, 'account/signup.html', {
            'form': form,
        })
