from pathlib import Path

#-- environment variables
#https://django-environ.readthedocs.io/en/latest/install.html
import environ
import os

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, True)
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = BASE_DIR / 'templates'
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'
#STATIC_ROOT = '/home/onkoto/www/static' # >>>> PRODUÇÃO  DESCOMENTAR
#MEDIA_URL = 'media/'
#MEDIA_ROOT = '/home/onkoto/www/media'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$@_bm0o@#@+%($@_2s=y6s!2$jv3$*cqmrxymij1xjojce7q&&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'www.onkoto.com.br', 'onkoto.com.br','[::1]', '*'] 

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'financas',
    'bootstrap5',
    'mathfilters',
    #'ckeditor',
    'django_adsense_injector',
    'django.contrib.sitemaps',
    'django_extensions', 
    'django_select2',  # 
    'jquery', 
    'django_tables2'#

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

ROOT_URLCONF = 'pool.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'pool.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# environment variables from .env file and compose-docker
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

SERVER_HOSTNAME     = os.environ.get('SECONDARY_SERVER_HOSTNAME', default= env('SERVER_HOSTNAME'))
DATABASE_NAME       = os.environ.get('SECONDARY_DATABASE_NAME', default= env('DATABASE_NAME'))
DATABASE_USER       = os.environ.get('SECONDARY_DATABASE_USER', default= env('DATABASE_USER'))
DATABASE_PASSWORD   = os.environ.get('SECONDARY_DATABASE_PASSWORD', default= env('DATABASE_PASSWORD'))


DATABASES = {
    # database geral
    'default'   : {
    'ENGINE'    :'django.db.backends.mysql',
    'NAME'      :DATABASE_NAME,
    'USER'      :DATABASE_USER,
    'PASSWORD'  :DATABASE_PASSWORD,
    'HOST'      :SERVER_HOSTNAME,
    'PORT'      :'3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True
DATE_INPUT_FORMATS = (
                           '%d/%m/%Y',              # '31/12/24'      
                           '%d/%m/%y',              # '10/25/06'                     
                             )

DECIMAL_SEPARATOR = u','
THOUSAND_SEPARATOR = u'.'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# authentication purposes
#LOGIN_URL = '/login/'
#LOGIN_REDIRECT_URL = '/main/'
#LOGOUT_REDIRECT_URL = '/login/'

# modo HTTPS
#SECURE_SSL_REDIRECT = True
#SESSION_COOKIE_SECURE = True
#CSRF_COOKIE_SECURE = True
#SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# caching with redis
# os.environ leitura do ambiente docker .yaml
REDIS_HOST = os.environ.get('REDIS_HOST', 'redis')
REDIS_PORT = os.environ.get('REDIS_PORT', '6379')

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://{}:{}/1".format(REDIS_HOST, REDIS_PORT),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "select2": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://{}:{}/2".format(REDIS_HOST, REDIS_PORT),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# Tell select2 which cache configuration to use:
SELECT2_CACHE_BACKEND = "select2"