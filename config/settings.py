"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path

import sentry_sdk
from django.utils.translation import gettext_lazy as _
from environs import Env
from sentry_sdk.integrations.django import DjangoIntegration

env = Env()
env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure--f(j&h391mtgax!p%4b(w^4iv_8hs3=))6t7n0=8v%2p7+-ao8"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", False)

ALLOWED_HOSTS = env.str("ALLOWED_HOSTS", "").split(",")

TELEGRAM_BOT_TOKEN = env.str("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = env.str("TELEGRAM_CHAT_ID", "")
GOOGLE_ANALYTICS_ID = env.str("GOOGLE_ANALYTICS_ID", "")
GOOGLE_TAG_MANAGER_ID = env.str("GOOGLE_TAG_MANAGER_ID", "")
GOOGLE_DOCS_URLS = {
    "en": {
        "light": (
            "https://docs.google.com/document/d/e/2PACX-1vQCLlwFR5DnGpron8daLgA0W9wfhVI3Pi95IztepnVOQlC5RbgBV"
            "-V2H61z8Falf9Ogx3RR2nC2_D-F/pub?embedded=true"
        ),
        "dark": (
            "https://docs.google.com/document/d/e/2PACX"
            "-1vTcqhXNj1L7QSc1jkO2Z8zSet_mG79668_k_5qkbSXzhDbM4nIK_aP4jxhp1nrhn7Bc45_N9RfSjMVj/pub?embedded=true"
        ),
    },
    "uz": {
        "light": "",
        "dark": "",
    },
}

GITHUB_REPO = "https://github.com/ChogirmaliYigit/chogirmali-blog"
CONTACT_EMAIL = "chogirmali.yigit@gmail.com"

PULL_COMMAND = env.str("PULL_COMMAND")
RESTART_COMMAND = env.str("RESTART_COMMAND")


# Application definition

INSTALLED_APPS = [
    "unfold",  # before django.contrib.admin
    "unfold.contrib.filters",  # optional, if special filters are needed
    "unfold.contrib.forms",  # optional, if special form elements are needed
    "unfold.contrib.import_export",  # optional, if django-import-export package is used
    "unfold.contrib.guardian",  # optional, if django-guardian package is used
    "unfold.contrib.simple_history",  # optional, if django-simple-history package is used
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "blog",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env.str("DB_NAME"),
        "USER": env.str("DB_USER"),
        "PASSWORD": env.str("DB_PASS"),
        "HOST": env.str("DB_HOST"),
        "PORT": env.str("DB_PORT"),
    },
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

EN = "en"
UZ = "uz"

LANGUAGES = (
    (EN, _("english")),
    (UZ, _("uzbek")),
)

LANGUAGE_CODE = "en-us"

LOCALE_PATHS = [
    os.path.join(BASE_DIR, "locale"),
]

TIME_ZONE = "Asia/Tashkent"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static/"]

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

DATA_UPLOAD_MAX_MEMORY_SIZE = 100 * 1024 * 1024

UNFOLD = {
    "show_search": True,
    "show_all_applications": True,
}

sentry_sdk.init(
    dsn="https://103e74c3092d514d4bb9bc31bac44fb7@o4506573970604032.ingest.sentry.io/4506574138507264",
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)
