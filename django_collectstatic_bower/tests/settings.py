"""Django settings module for test environment"""
import os

INSTALLED_APPS = (
	'django_collectstatic_bower',
	'django.contrib.staticfiles',
)

SECRET_KEY = os.urandom(40)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.getcwd(), 'static')

MEDIA_URL = '/media/'
