"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-c-w6ubhs!j^w)r&lsc1^ubjf%jmncw%goyr@-&#0!9hh1-h=2!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [

    '192.168.0.110',
    '127.0.0.1'
    # '192.168.22.168'
    # '.vercel.app',
    # '.now.sh'
]

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    # 'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main_control',
    'clg_admin.apps.ClgAdminConfig',
    'dept_admin',
    'dept_faculty'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # 'main_control.middleware.AdminModelMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # os.path.join(BASE_DIR),
            BASE_DIR / 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Calcutta'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'

# Directories where Django will look for static files during development
STATICFILES_DIRS = [
    BASE_DIR / "static",  # Change this to a different directory, not the one used in STATIC_ROOT
]

# Directory where Django will collect static files for production
# STATIC_ROOT = BASE_DIR / 'static'  # This should be different from any in STATICFILES_DIRS

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# configuring django authentication for defining custom auth
AUTH_USER_MODEL = 'main_control.CustomUser'

JAZZMIN_SETTINGS = {
    "site_title": "AASC-ST-ASMT-MANGER",
    "site_header": "AASC-MANAGER",
    "site_logo": "backend/assets/img/achariya.png",
    "site_brand": "AASC-Administration",
    "copyright": "Vigneshwaran <br>Your Vision, My Creation ",
    "site_logo_classes": "img-circle",
    "welcome_sign": "Welcome to the AASC Assessment Management System",
    "use_google_fonts_cdn": True,
    "related_modal_active": False,
    "show_ui_builder": True,
    "custom_css": "admin/custom.css",
    # Icons are from fontawesome
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "main_control.CustomUser": "fas fa-users",
    },

    # "custom_links": {
    #     "clg_admin": [{
    #         "name": "Manage Internals",
    #         "url": "/internals/manage_internals/",
    #         "icon": "fas fa-comments",
    #         # "permissions": ["faculty.view_faculty"]
    #     }]
    # },
    "changeform_format": "carousel",

}
JAZZMIN_UI_TWEAKS = {

    "theme": "lux",
    "dark_mode_theme": "solar",
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'venerablevignesh@gmail.com'
EMAIL_HOST_PASSWORD = 'drftcutfbaizkniy'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
LOGIN_REDIRECT_URL = '/admin/'  # Redirect to Django admin dashboard
