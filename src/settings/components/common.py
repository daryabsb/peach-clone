from src.settings.components.env import config
from tzlocal import get_localzone
from src.settings.components import PROJECT_PATH

BASE_ENDPOINT = config('BASE_ENDPOINT', default='http://127.0.0.1:8000')
WS_ENDPOINT = config('WS_ENDPOINT', default='ws://127.0.0.1:8000')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
SITE_ID = 1

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 's%ur6m9zh59%#k#6kgtb4aqe&1#l$e)71zv8d9(095ft00&7^l'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# ALLOWED_HOSTS = ["127.0.0.1", "172.16.10.49", "62.201.232.212"]


# Application definition
DJANGO_APPS = [
    'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # 'allauth',
    # 'allauth.account',
    "django_extensions",
    "django_htmx",
    "debug_toolbar",

    'django.contrib.staticfiles',
    'django.contrib.humanize',

    'after_response',
    'rest_framework',
    'channels',
]

THIRD_PARTY_APPS = [
    'crispy_forms',
    'widget_tweaks',
    'bootstrap4',
    'django_cotton',
    'django_celery_beat',
    'django_celery_results',
    'django_filters',
    'fontawesome_5',
]

LOCAL_APPS = [
    'src.accounts',
    'src.core',
    'src.finances',
    'src.users',
    'src.transactions',
    'src.statement',
    'src.company',
    'src.sales',
    'src.purchase',

]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

AUTH_USER_MODEL = 'accounts.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django_htmx.middleware.HtmxMiddleware",
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'src.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            PROJECT_PATH + "\\templates",
            PROJECT_PATH + "\\accounts\\templates",
            PROJECT_PATH + "\\company\\templates",


            ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'custom_context_processor.dz_static',
            ],
        },
    },
]

WSGI_APPLICATION = 'src.wsgi.application'
ASGI_APPLICATION = 'src.asgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases




# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


CRISPY_TEMPLATE_PACK = 'uni_form'
