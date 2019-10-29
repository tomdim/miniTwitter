from .base import *


# Debug django toolbar
INSTALLED_APPS += ('debug_toolbar', )
MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'debug_toolbar_force.middleware.ForceDebugToolbarMiddleware',
]
INTERNAL_IPS = ['127.0.0.1', ]

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('VH_DATABASE_NAME', 'mini_twitter'),
        'USER': os.environ.get('VH_DATABASE_USER', 'postgres'),
        'PASSWORD': os.environ.get('VH_DATABASE_PASS', '1234'),
        'HOST': os.environ.get('VH_DATABASE_HOST', 'localhost'),
        'PORT': os.environ.get('VH_DATABASE_PORT', '5432'),
    },
}
