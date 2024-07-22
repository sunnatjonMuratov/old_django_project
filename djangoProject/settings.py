#!/usr/bin/env  python
import os.path
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-%dp@))kvue-f+%ohq=*grv9w46$b%%#sz2@t*sypatut1(u(pr'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djangoProject.urls'

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

WSGI_APPLICATION = 'djangoProject.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 1,
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


JAZZMIN_SETTINGS = {
    'site_title': 'My Admin',

    'site_header': 'My Admin',

    'site_logo': 'apps/logo.png',

    'user_avatar': 'apps/logo.png',

    'site_logo_text': 'My Admin',

    'welcome_sign': 'Welcome to My Admin',

    'copyright': 'My Company',

    'search_model': 'auth.User',


    'topmenu_links': [
        {'name': 'Home', 'url': 'admin:index', 'permissions': ['auth.view_user']},

        {'name': 'Support', 'url': 'https://github.com/farridav/django-jazzmin/issues', 'new_window': True},

        {'model': 'auth.User'},

        {'app': 'books'},
    ],

    'hide_apps': [],

    'icons': {
        'auth': 'fas fa-users-cog',
        'auth.user': 'fas fa-user',
        'auth.Group': 'fas fa-users',
    },

    'use_modals': False,

    'show_sidebar': True,

    'navigation_expanded': True,

    'hide_models': [],

    'custom_links': {
        'books': [{
            'name': 'Make Messages',
            'url': 'make_messages',
            'icon': 'fas fa-comments',
            'permissions': ['books.view_book']
        }]
    },

    'related_modal_active': False,

    'custom_css': None,
    'custom_js': None,
    'use_google_fonts_cdn': True,
    'show_ui_builder': False,

    'show_search': True,
}


AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR / 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
