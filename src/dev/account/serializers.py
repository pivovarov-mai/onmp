from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from .models import User


class UserSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')

    def validate(self, attrs):
        try:
            validate_password(attrs['password'])
        except ValidationError as e:
            raise serializers.ValidationError({'password': str(e)})
        return super().validate(attrs)


class UserSerializerMinimum(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'is_email_confirmed')

    def save(self, **kwargs):
        User.objects.create_user(
            email=self.validated_data['email'],
            password=self.validated_data['password'])


class UserSerializerMaximum(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'is_email_confirmed',
                  'is_admin', 'is_active', 'date_joined')


class UserSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', 'groups', 'user_permissions')
