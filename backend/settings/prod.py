""" Production Settings """
import dj_database_url
from decouple import config
from .base import *

############
# DATABASE #
############
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}

############
# SECURITY #
############

DEBUG = config('DJANGO_DEBUG', cast=bool, default=False)

SECRET_KEY = config('DJANGO_SECRET_KEY')

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])

CORS_ORIGIN_WHITELIST = [
   "http:" + config('VUE_APP_BASEURL'),
   "https:" + config('VUE_APP_BASEURL'),
#    config('VUE_APP_BASEURL')
]