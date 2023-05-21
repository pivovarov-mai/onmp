import os, environ
from pathlib import Path

env = environ.Env()
env.read_env('../.env.prod')

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env('SECRET', default='django-insecure-ve6j717og63l80j*fz$1krifzkoq7!8ban2l%^*ogj5b)oiyae')

DEBUG = env('DEBUG', default='True') == 'True'

ALLOWED_HOSTS = env('ALLOWED_HOSTS').split(' ') \
    if 'ALLOWED_HOSTS' in env else []

INSTALLED_APPS = [
    'jazzmin',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'drf_yasg',

    'account',
    'diagnoses',
    'diseases',
    'medicines',
    'differentials_diag',

    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': env('POSTGRES_ENGINE', default='django.db.backends.sqlite3'),
        'NAME': env('POSTGRES_DB', default=os.path.join(BASE_DIR, 'db.sqlite3')),
        'USER': env('POSTGRES_USER', default=''),
        'PASSWORD': env('POSTGRES_PASSWORD', default=''),
        'HOST': env('POSTGRES_HOST', default='localhost'),
        'PORT': env('POSTGRES_PORT', default='5432'),
    },
}


CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.PyMemcacheCache",
        "LOCATION": "127.0.0.1:11211",
    },
    "debug": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "unique-snowflake",
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'
STATIC_ROOT = env('STATIC_ROOT', default='collectedstatic/')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_URL = 'media/'
MEDIA_ROOT = 'collectedmedia/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CARD_RANGE_START    = 0
CARD_RANGE_END      = 999_999_999

AUTH_USER_MODEL = 'account.User'
LOGOUT_REDIRECT_URL = 'home'

# CORS
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=465 # or 587 if tls
EMAIL_HOST_USER='onmp.ru@gmail.com'
EMAIL_HOST_PASSWORD=env('EMAIL_PASSWORD', default='')
# EMAIL_USE_TLS = True
EMAIL_USE_SSL = True

CSRF_TRUSTED_ORIGINS = ['http://188.225.78.148', 'http://*.127.0.0.1']

DOMEN = env('DOMEN', default='http://localhost:8000')

CELERY_BROKER_URL = env('CELERY_BROKER_URL', default='')
CELERY_RESULT_BACKEND = env('CELERY_RESULT_BACKEND', default='')
