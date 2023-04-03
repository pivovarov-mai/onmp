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
    get_user_model,
)
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication,
)
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
    AllowAny,
)
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .forms import UserLoginForm, UserRegisterForm
from .serializers import (
    UserSerializerDetail,
    UserSerializerMinimum,
    UserSerializerCreate,
)
from .swagger import (
    SW_GET_TOKEN,
    SW_CREATE_USER,
    SW_GET_PROFILE,
)


class UserGetTokenAPI(APIView):
    '''
    Api for getting token by user fields(email, password) in POST method or by session auth
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
            return Response({'token':
                Token.objects.get_or_create(user=user)[0].key})
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
            get_user_model().objects.create_user(
                user_ser.validated_data['email'],
                user_ser.validated_data['password'],
                user_ser.validated_data['first_name'],
                user_ser.validated_data['last_name'],
                mail_denied=request.data.get('mail_denied', False))
            return Response({'success'}, status=status.HTTP_201_CREATED)
        return Response(user_ser.errors, status=status.HTTP_418_IM_A_TEAPOT)


class GetProfileAPI(APIView):
    '''
    Get profile data for user by token
    '''

    @swagger_auto_schema(**SW_GET_PROFILE)    
    def get(self, request):
        if 'HTTP_AUTHORIZATION' not in request.META:
            return Response({
                'error': 'В заголовках надо указать токен авторизации'},
                status=status.HTTP_418_IM_A_TEAPOT)
            
        token = Token.objects.filter(
            key=request.META['HTTP_AUTHORIZATION'][6:])
        if not token.exists():
            return Response({'error': 'Токен неверен или несуществует'},
                            status=status.HTTP_418_IM_A_TEAPOT)

        return Response({'user':
            UserSerializerMinimum(instance=token.first().user).data},
                        status=status.HTTP_200_OK)


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
