import os
import sys
import path

# Celery init
import djcelery
djcelery.setup_loader()

PROJECT_PATH = path.path(__file__).parent.parent
PROJECT_NAME = PROJECT_PATH.name
PROJECT_LOCAL = PROJECT_PATH.parent / 'local'

# Django settings for jtg project.

PROJECT_DOMAIN = ''
PROJECT_URL = PROJECT_DOMAIN
SESSION_COOKIE_DOMAIN = ''
#CSRF_COOKIE_DOMAIN = SESSION_COOKIE_DOMAIN

sys.path.append(PROJECT_PATH)
PACKAGES = (
    'apps',
    'conf',
)

for package in PACKAGES:
    sys.path.append(PROJECT_PATH / package)

SHARED_ENV = PROJECT_LOCAL / 'shared_env'

SHARED_PACKAGES = (
)

sys.path.append(SHARED_ENV)
for env in os.listdir(SHARED_ENV):
    sys.path.append(SHARED_ENV / env)

for package in SHARED_PACKAGES:
    sys.path.append(SHARED_ENV / package)


DEBUG = False
VERBOSE = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('Jesse Zwaan', 'j.k.zwaan@gmail.com'),
)

MANAGERS = ADMINS

from fnmatch import fnmatch
class glob_list(list):
    def __contains__(self, key):
        for elt in self:
            if fnmatch(key, elt): return True
        return False

INTERNAL_IPS = glob_list([
    '127.0.0.1',
])

LANGUAGE_CODE = 'en-us'

USE_I18N = False

MEDIA_ROOT = PROJECT_PATH / 'media'

STATIC_URL = ''
IMAGES_URL = '%s/img/' % STATIC_URL

MEDIA_URL = '/assets/' # 'http://static.%s/' % PROJECT_URL

MIDDLEWARE_CLASSES = (
    #'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.cache.FetchFromCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',

)

ROOT_URLCONF = '%s.conf.urls' % PROJECT_NAME

TEMPLATE_DIRS = (
    PROJECT_PATH / 'templates',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.webdesign',

    PROJECT_NAME,

    'djcelery',
    'kombu.transport.django',

)

LOGIN_URL = ''
LOGIN_REDIRECT_URL = ''
LOGIN_ERROR_URL = ''

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.ModelBackend',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",

    "%s.context_processors.static" % PROJECT_NAME,
)

#SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"

CELERY_IMPORTS = [
]
