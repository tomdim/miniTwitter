from .development import *

TESTING = True

INSTALLED_APPS.remove('debug_toolbar')
MIDDLEWARE.remove('debug_toolbar.middleware.DebugToolbarMiddleware')
MIDDLEWARE.remove('debug_toolbar_force.middleware.ForceDebugToolbarMiddleware')
INTERNAL_IPS.remove('127.0.0.1')
