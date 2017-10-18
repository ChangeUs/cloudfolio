from .base import *
# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_local',
    }
}

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'statics/')]