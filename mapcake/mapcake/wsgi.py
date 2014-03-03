"""
WSGI config for mapcake project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

from os import environ
environ.setdefault("DJANGO_SETTINGS_MODULE", "mapcake.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
