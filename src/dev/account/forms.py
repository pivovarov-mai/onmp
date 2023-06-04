from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password"""
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтверждение пароля',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'is_admin', 'is_active')


class UserLoginForm(forms.Form):
    """A form for loging users. Includes only email and password"""
    email = forms.EmailField(max_length=20,
                             label='Email почта',
                             help_text='Введите свою email почту')
    password = forms.CharField(widget=forms.PasswordInput,
                               label='Пароль')

    def is_valid(self):
        valid = super().is_valid()
        if not valid:
            return False
        if not User.objects.filter(email=self.cleaned_data['email']).exists():
            self.errors['email'] = ['Пользователь не найден',]
            return False
        return True


class UserRegisterForm(forms.Form):
    '''A form for registration new users because of form above doesn't save'''
    email = forms.EmailField(label='Email почта')
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтверждение пароля',
                                widget=forms.PasswordInput)

    def is_valid(self):
        valid = super().is_valid()
        if not valid:
            return False
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.errors['password1'] = ['Пароли не совпадают',]
            return False
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            self.errors['email'] = ['Пользователь уже существует',]
            return False
        return True
