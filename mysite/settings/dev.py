from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-ji=^47^&qlpd2$fq5qb&pyz(*c6b1+a_pjo2ol_-+4l#6_s@px"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass
