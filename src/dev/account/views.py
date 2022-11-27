from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model

from .forms import UserLoginForm, UserRegisterForm


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
