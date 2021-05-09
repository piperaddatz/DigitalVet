from .base import *


DEBUG = True

ALLOWED_HOSTS = ['digitalvet.herokuapp.com']
#'digitalvet.herokuapp.com'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': BASE_DIR / 'dcmubvcvtdam9t',
        'USER': 'ebmixetjwrcwap',
        'PASSWORD': '131e117d99c6a968110ebb47cd11fc06f1192492c6e6c7458fa4ac39da04b67f',
        'HOST': 'ec2-18-206-20-102.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}


STATICFILES_DIRS = (BASE_DIR, 'static')