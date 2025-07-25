import os
from pathlib import Path

from django_ledger.settings import DJANGO_LEDGER_GRAPHQL_SUPPORT_ENABLED

BASE_DIR = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

SECRET_KEY = os.getenv('SECRET_KEY')
if not SECRET_KEY:
    SECRET_KEY = '&9b7(-8cp5)mkz4j8kz*o_%njy944qn1p69ojdz35ui97)_ai8'
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '192.168.1.102', 'localhost']
CSRF_TRUSTED_ORIGINS = ['https://*.preview.app.github.dev']

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django_ledger',
    'website',
    'post_media',
    'ckeditor',
    'ckeditor_uploader',
    'dashboard',
    'ledger',
    'leads',
]

if DJANGO_LEDGER_GRAPHQL_SUPPORT_ENABLED:
    INSTALLED_APPS += [
        'graphene_django',
        'oauth2_provider'
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

ROOT_URLCONF = 'dev_env.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'dev_env.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases


import pymysql
pymysql.install_as_MySQLdb() 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'erp_lab',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}



#DATABASES = {
#   'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

USE_TZ = False
TIME_ZONE = 'Asia/Jakarta'

USE_I18N = True
USE_L10N = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_ROOT = os.path.join(BASE_DIR, 'static')  # kamu bisa sesuaikan nama foldernya


STATIC_URL = '/static/'
LOGIN_URL = '/auth/login/'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

if DJANGO_LEDGER_GRAPHQL_SUPPORT_ENABLED:
    GRAPHENE = {
        'SCHEMA': 'django_ledger.contrib.django_ledger_graphene.api.schema',
        'SCHEMA_OUTPUT': '../django_ledger/contrib/django_ledger_graphene/schema.graphql',  # defaults to schema.json,
        # 'SCHEMA_INDENT': 2,  # Defaults to None (displays all data on a single line)
        # 'MIDDLEWARE': [
        #     'graphql_jwt.middleware.JSONWebTokenMiddleware',
        # ],
    }

    OAUTH2_PROVIDER = {
        'OAUTH2_BACKEND_CLASS': 'oauth2_provider.oauth2_backends.JSONOAuthLibCore',
    }

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379',
    }
}

# settings.py
DJANGO_LEDGER_CURRENCY_SYMBOL = 'Rp'
DJANGO_LEDGER_SPACED_CURRENCY_SYMBOL = True  # Jika ingin hasil seperti: Rp 1.000,00


# LOGGING = {
#     'version': 1,
#     'filters': {
#         'require_debug_true': {
#             '()': 'django.utils.log.RequireDebugTrue',
#         }
#     },
#     'handlers': {
#         'console': {
#             'level': 'DEBUG',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#         }
#     },
#     'loggers': {
#         'django.db.backends': {
#             'level': 'DEBUG',
#             'handlers': ['console'],
#         }
#     }
# }
CKEDITOR_UPLOAD_PATH = "uploads/"
