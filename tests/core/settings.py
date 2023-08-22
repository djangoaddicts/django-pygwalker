"""
Minimal file for unittest configs.
"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = "test"

# INSTALLED_APPS with these apps is necessary for Sphinx to build
# without warnings & errors
# Depending on your package, the list of apps may be different
INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "djangoaddicts.pygwalker",
    "handyhelpers",
    "tests.core.testapp",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "tests.core.urls"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "db.sqlite3",
        "TEST_NAME": "test.sqlite3",
        "USER": "djangoaddicts",
        "PASSWORD": "djangoaddicts",
    }
}

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "core", "templates")],
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

BASE_TEMPLATE = "base.htm"

USE_TZ = True
