from .base import *


DEBUG = True

ALLOWED_HOSTS = ['*']
#'digitalvet.herokuapp.com'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


STATICFILES_DIRS = (BASE_DIR, 'static')