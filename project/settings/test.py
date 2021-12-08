import os
from .settings import *

DEBUG = 'True'

DATABASES['default'].update({
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': 'mydatabase',
})

CACHES = {
    'default': {'BACKEND': 'django.core.cache.backends.dummy.DummyCache',}
}