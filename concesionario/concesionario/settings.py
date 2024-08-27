# concesionario/settings.py

import os
from pathlib import Path
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

# Building paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Initialize Sentry SDK
sentry_sdk.init(
    dsn="https://e79ad569fda166a3422b235afc96a356@o4507817652125696.ingest.us.sentry.io/4507817661300736",
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)

# Load environment variables from .env file
def load_env_file():
    env_path = BASE_DIR / '.env'
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                if line.startswith('#') or '=' not in line:
                    continue
                key, value = line.strip().split('=', 1)
                os.environ.setdefault(key, value)

# Load the .env file
load_env_file()

# Security settings
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'default-secret-key-for-development-only')
DEBUG = True  
ALLOWED_HOSTS = ['*']  # Add allowed domains or IPs in production

# Installed applications
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'vehicles',
    'media',
    'users',
    'comments',
    'storages',  # Added for django-storages
]

# Middleware configuration
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL configuration
ROOT_URLCONF = 'concesionario.urls'

# Template settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Global template folder
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'concesionario.context_processors.dealership_info',
                'users.context_processors.user_status',
            ],
        },
    },
]

# WSGI configuration
WSGI_APPLICATION = 'concesionario.wsgi.application'

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files configuration
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# AWS S3 Configuration
AWS_STORAGE_BUCKET_NAME = 'djangoitec'
AWS_S3_REGION_NAME = 'us-east-2'  # US East (Ohio)
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

# Use S3 for storing media files
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'

# Remove MEDIA_ROOT as files are not stored locally
# MEDIA_ROOT = BASE_DIR / 'media'

# Optional S3 settings
AWS_S3_FILE_OVERWRITE = False  # Prevents overwriting files with the same name
AWS_DEFAULT_ACL = 'public-read'  # Manage file permissions
AWS_QUERYSTRING_AUTH = False  # Prevents URLs from having authentication tokens

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Redirect to the profile login
LOGIN_REDIRECT_URL = 'profile'

# Logout redirection
LOGOUT_REDIRECT_URL = 'home'  

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'django_debug.log'),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
