from django.apps import AppConfig
from django.conf import settings, global_settings


class DjangoBowerConfig(AppConfig):
	"""Automatically hook up finder if necessary"""

	name = 'django_collectstatic_bower'
	verbose_name = 'Django Collectstatic Bower'

	def auto_configure_finder(self):
		if getattr(settings, 'BOWER_AUTO_CONFIGURE', True):
			if not hasattr(settings, 'STATICFILES_FINDERS'):
				settings.STATICFILES_FINDERS = global_settings.STATICFILES_FINDERS

			settings.STATICFILES_FINDERS += ('django_collectstatic_bower.staticfiles.finders.BowerComponentFinder',)

	def ready(self):
		self.auto_configure_finder()
