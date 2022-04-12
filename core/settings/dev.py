from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'kyle',
#         'USER': 'root',
#         'PASSWORD': 'root',
#         'HOST': 'localhost',
#         'PORT': '3306',
#     },
#     'read-only' : {
#         'ENGINE' : 'django.db.backends.postgresql',
#         'NAME' : 'database_name',
#         'USER' : 'root',
#         'PASSWORD' : 'root',
#         'HOST' : 'localhost',
#         'PORT' : '5432',
#         'ATOMIC_REQUESTS': True,
#     },
# }
