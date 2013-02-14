import site
import path

ROOT = path.path(__file__).parent.parent.parent
LOCAL = ROOT.parent / 'local'

site.addsitedir(ROOT)

PACKAGES = (
    'apps',
    'libs',
)

for package in PACKAGES:
    if path.path(ROOT / package).isdir():
        site.addsitedir(ROOT / package)

DEBUG = False
VERBOSE = False
TEMPLATE_DEBUG = DEBUG

SESSION = True
SOUTH = False
CELERY = False
CACHE = False

USE_I18N = False

ADMINS = (
     ('Jesse Zwaan', 'j.k.zwaan@gmail.com'),
)

MANAGERS = ADMINS

from fnmatch import fnmatch
class glob_list(list):
    """Allows wildcards in ip addresses"""
    def __contains__(self, key):
        for elt in self:
            if fnmatch(key, elt): return True
        return False

INTERNAL_IPS = glob_list([
    '127.0.0.1',
])

LANGUAGE_CODE = 'en-us'

STATIC_URL = '/static'
STATIC_ROOT = LOCAL / 'static'

STATICFILES_DIRS = (
    SOURCE / 'assets',
)

MEDIA_URL = '/media'
MEDIA_ROOT = LOCAL / 'media'

ROOT_URLCONF = 'conf.urls'

WSGI_APPLICATION = 'entry.application'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
)

TEMPLATE_DIRS = (
    ROOT / 'templates',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.webdesign',
    'django.contrib.staticfiles',

    'utils',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.ModelBackend',
)

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
TEMPLATE_CONTEXT_PROCESSORS += (
    "conf.context_processors.static",
)

if CACHE:
    common = 'django.middleware.common.CommonMiddleware'
    update = 'django.middleware.cache.UpdateCacheMiddleware'
    fetch = 'django.middleware.cache.FetchFromCacheMiddleware'
    try:
        index = tup.index(common)
    except ValueError:
        MIDDLEWARE_CLASSES = (update, fetch) + MIDDLEWARE_CLASSES
    else:
        MIDDLEWARE_CLASSES = (update, common, fetch) + MIDDLEWARE_CLASSES[:index] + MIDDLEWARE_CLASSES[index + 1:]

if SOUTH:
    INSTALLED_APPS += (
        'south',
    )


if SESSION:
    SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"
    INSTALLED_APPS += (
        'django.contrib.sessions',
    )
    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
    )



if CELERY:
    INSTALLED_APPS += (
        'djcelery',
        'kombu.transport.django',
    )

    CELERY_IMPORTS = [
        'myapp.tasks',
    ]

    import djcelery
    djcelery.setup_loader()
