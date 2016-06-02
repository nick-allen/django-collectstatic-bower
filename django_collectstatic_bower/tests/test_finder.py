from unittest import TestCase
from unittest.mock import patch

from nose.tools import assert_equal


class FinderTests(TestCase):

	def setUp(self):
		from django_collectstatic_bower.staticfiles.finders import BowerComponentFinder
		self.finder = BowerComponentFinder()

	@patch('django_collectstatic_bower.bower.bower')
	def test_finder_runs_bower_install(self, bower_mock):
		"""Verify bower install is done before finding or collecting static files"""

		self.finder.list([])

		self.finder.find('')

		assert_equal(bower_mock.call_count, 2)
		bower_mock.assert_called_with('install')

	def test_finder_list(self):
		"""Verify list yields all files installed by bower"""

	def test_finder_find(self):
		"""Tests that the finder supports the findstatic command"""

	def test_finder_autoconfigured(self):
		"""Tests that the finder is automatically installed if app listed in INSTALLED_APPS"""
