from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tale_teller',
        'USER': 'elongton',
        'PASSWORD': 'puttie',
        'HOST': 'localhost',
        'PORT': '',
    }
}
