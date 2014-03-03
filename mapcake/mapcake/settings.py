"""
Django settings for mapcake project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '19d63k2c3l@$a89sa*4q%ocirsh@38*l&vw#9qf47xc%xwgx*!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'accounts',
    'userena', # To Delete in prod? This allows to use de commands check_permissions and clean_expired whith manage.py
    'guardian',
    'easy_thumbnails',
    'layers',
    #'debug_toolbar', # To Delete in prod
    'south',
    'maps',
)

MIDDLEWARE_CLASSES = (
    # Django debug toolbar app
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Userena app
    'userena.middleware.UserenaLocaleMiddleware',
)

ROOT_URLCONF = 'mapcake.urls'

WSGI_APPLICATION = 'mapcake.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',  # Add
        # 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'mapcake',  # Or path to database file if using
        # sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'David',
        'PASSWORD': 'zomadic',
        'HOST': 'localhost',  # Empty for localhost through domain sockets or
        # '127.0.0.1' for localhost through TCP.
        'PORT': '5432',  # Set to empty string for default.
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

# Template dir
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "templates"),
)
### USERENA SETTINGS 11-12-2013
# Userena configuration backends

AUTHENTICATION_BACKENDS = (
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)

ANONYMOUS_USER_ID = -1 

AUTH_PROFILE_MODULE = 'accounts.MyProfile'

LOGIN_REDIRECT_URL = '/accounts/%(username)s/'
LOGIN_URL = '/accounts/signin/'
LOGOUT_URL = '/'
SITE_ID = 1

# Email configuration for userena

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

CONTEXT_PROCESSORS = (
    'django.core.context_processors.csrf',
)

# Django-Debug-Toolbar configuration

# INTERNAL_IPS = ('127.0.0.1','127.0.0.1:8000')

# DEBUG_TOOLBAR_PANELS = (
#     'debug_toolbar.panels.version.VersionDebugPanel',
#     'debug_toolbar.panels.timer.TimerDebugPanel',
#     'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
#     'debug_toolbar.panels.headers.HeaderDebugPanel',
#     'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
#     'debug_toolbar.panels.template.TemplateDebugPanel',
#     'debug_toolbar.panels.sql.SQLDebugPanel',
#     'debug_toolbar.panels.signals.SignalDebugPanel',
#     'debug_toolbar.panels.logger.LoggingPanel',
#     #'cache_panel.CachePanel',
# )

# def custom_show_toolbar(request):
#     return True  # Always show toolbar, for example purposes only.

# DEBUG_TOOLBAR_CONFIG = {
#     'INTERCEPT_REDIRECTS': True,
#     'SHOW_TOOLBAR_CALLBACK': custom_show_toolbar,
#     'EXTRA_SIGNALS': ['myproject.signals.MySignal'],
#     'HIDE_DJANGO_SQL': False,
#     'TAG': 'div',
#     'ENABLE_STACKTRACES': True,
#   }
