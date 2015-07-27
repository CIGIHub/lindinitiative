from __future__ import absolute_import, unicode_literals
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$97_hxreviqoq^zl11mpk7mswo&&kt4k7g(t)v)0m_u5_k+i!h'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'lindinitiative',
        'USER': 'lindinitiative',
    }
}

try:
    from .local import *
except ImportError:
    pass
