from django.contrib.staticfiles.finders import BaseStorageFinder
from django.core.files.storage import FileSystemStorage

from django_collectstatic_bower import bower


class BowerComponentFinder(BaseStorageFinder):
	"""Finder that returns bower components, installing them if necessary"""

	storage = FileSystemStorage(bower.get_bower_components_path())

	def install_components(self):
		bower.bower('install')

	def find(self, path, all=False):
		self.install_components()

		return super(BowerComponentFinder, self).find(path, all)

	def list(self, ignore_patterns):
		"""Installs bower components listed in bower.json, then lists all installed files"""
		self.install_components()

		return super(BowerComponentFinder, self).list(ignore_patterns)
