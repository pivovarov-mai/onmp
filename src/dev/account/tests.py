import uuid
from unittest import skipIf

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.conf import settings
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

USER_MODEL = get_user_model()


class AccountTests(TestCase):
    def test_user_creation(self):
        user = USER_MODEL.objects.create_user(
            email='test@test.ru',
            password='password_test',
            first_name='ivan',
            last_name='ivanov',
        )
        self.assertEqual(user.email, 'test@test.ru')
        self.assertTrue(user.check_password('password_test'))
        self.assertEqual(user.first_name, 'ivan')
        self.assertEqual(user.last_name, 'ivanov')

    def test_superuser_creation(self):
        user = USER_MODEL.objects.create_superuser(
            email='test@test.ru',
            password='password_test',
            first_name='ivan',
            last_name='ivanov',
        )
        self.assertEqual(user.email, 'test@test.ru')
        self.assertTrue(user.check_password('password_test'))
        self.assertEqual(user.first_name, 'ivan')
        self.assertEqual(user.last_name, 'ivanov')
        # self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_admin)


class UserAPITests(APITestCase):
    password = 'test'

    def setUp(self):
        self.user = USER_MODEL.objects.create_user(
            email='test@test.ru',
            password=self.password,
            first_name='ivan',
            last_name='ivanov',
        )
        self.token = Token.objects.create(user=self.user).key

    def test_get_token(self):
        # Check created user
        self.assertEqual(self.user.email,
                         'test@test.ru',
                         'User has not been created')

        # Some requried variables for requests
        url = reverse('token')
        data = {'email': self.user.email,
                'password': self.password}

        # Check error while not confirmed email
        response_bad = self.client.post(url, data, format='json')
        self.assertEqual(response_bad.status_code, 401)
        self.assertEqual(response_bad.data['error'], 'Подтвердите email')

        # Check error with bad credentials
        response_bad = self.client.post(url,
                                        {'email': self.user.email + 'a',
                                         'password': self.password},
                                        format='json')
        self.assertEqual(response_bad.status_code, 401)
        self.assertEqual(response_bad.data['error'],
                         'Данные пользователя неверны, либо вы не авторизованны')

        # Make email confirmed
        self.user.is_email_confirmed = True
        self.user.save()

        # Check good request and get normal token
        response_good = self.client.post(url, data, format='json')
        self.assertEqual(response_good.status_code, 200)

        # Memory token for future use
        self.assertTrue(Token.objects.get().key, self.token)

    def test_get_user_profile(self):
        url = reverse('user_profile')

        # Check error without token in header
        response = self.client.get(url)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data['detail'],
                         'Учетные данные не были предоставлены.')

        # Check error with wrong token
        self.client.credentials(
            HTTP_AUTHORIZATION='Token ' + self.token + '1'
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data['detail'],
                         'Недопустимый токен.')

        # Check good
        self.client.credentials(
            HTTP_AUTHORIZATION='Token ' + self.token
        )
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['user']['first_name'],
                         self.user.first_name)

    def get_response_by_account_create(self, credentials):
        url = reverse('user_create')
        return self.client.post(url, data=credentials)

    def test_create_user_account(self):
        url = reverse('user_create')
        credentials = {
            'email': 'a@a.r',
            'password': 'test123',
            'first_name': 'andrey',
            'last_name': 'uvarov',
        }

        # Bad email
        response = self.get_response_by_account_create(credentials)
        self.assertEqual(response.status_code, 400)

        # Bad password
        credentials['password'] = 'test'
        credentials['email'] = 'a@a.ru'
        response = self.get_response_by_account_create(credentials)
        self.assertEqual(response.status_code, 400)

        # First name does not exists
        credentials['password'] = 'test123_test'
        del credentials['first_name']
        response = self.get_response_by_account_create(credentials)
        self.assertEqual(response.status_code, 400)

        # Last name does not exists
        credentials['first_name'] = 'andrey'
        del credentials['last_name']
        response = self.get_response_by_account_create(credentials)
        self.assertEqual(response.status_code, 400)

        # Good one
        credentials['last_name'] = 'uvarov'
        credentials['mail_denied'] = True
        response = self.get_response_by_account_create(credentials)
        created_user = get_user_model().objects.filter(email='a@a.ru')
        self.assertTrue(created_user.exists())
        created_user = created_user[0]
        self.assertEqual(created_user.email, 'a@a.ru')
        self.assertTrue(created_user.check_password('test123_test'))
        self.assertEqual(created_user.first_name, 'andrey')
        self.assertEqual(created_user.last_name, 'uvarov')

    def test_email_confirmation_api(self):
        # Good
        id = self.user.email_id
        url = reverse('email_confirm', kwargs={'id': id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # Error
        id = list(str(self.user.email_id))
        id[0] = 'a'
        id = ''.join(id)
        url = reverse('email_confirm', kwargs={'id': id})
        response = self.client.get(url)
        self.assertEqual(response.data['error'], 'Пользователь не существует')
        self.assertEqual(response.status_code, 401)
