from unittest import TestCase
from mock import patch

from nose.tools import assert_equal


mock_bower = patch('django_collectstatic_bower.bower.bower')


class FinderTests(TestCase):

	def setUp(self):
		from django_collectstatic_bower.staticfiles.finders import BowerComponentFinder
		self.finder = BowerComponentFinder()

	@mock_bower
	def test_finder_runs_bower_install(self, bower_mock):
		"""Verify bower install is done before finding or collecting static files"""

		self.finder.list([])

		self.finder.find('')

		assert_equal(bower_mock.call_count, 2)
		bower_mock.assert_called_with('install')

