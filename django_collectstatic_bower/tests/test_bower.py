"""Tests bower adapter"""
import os
import mock

from django.test import override_settings
from nose.tools import assert_equal

from django_collectstatic_bower import bower


@mock.patch('django_collectstatic_bower.bower.get_bower_executable_path')
@mock.patch('subprocess.Popen')
def test_bower_subprocess(subprocess_mock, exe_path_mock):
	"""Tests that the provided bower executable is launched in a subprocess"""
	exe_path = '/path/to/bower'
	cmd = 'install'
	cwd = os.getcwd()

	exe_path_mock.return_value = exe_path
	proc_mock = mock.Mock()
	proc_mock.configure_mock(**{
		'wait': lambda: None,
		'returncode': 0
	})
	subprocess_mock.return_value = proc_mock

	bower.bower(cmd)

	subprocess_mock.assert_called_with((exe_path, cmd), cwd=cwd)


def test_bower_get_executable():
	"""Tests that the get_bower_cmd() finds the path to the bower executable"""
	# Verify django settings override option
	with override_settings(BOWER_CMD='/override/path'):
		assert_equal(bower.get_bower_executable_path(), '/override/path')

	with override_settings():
		with mock.patch('django_collectstatic_bower.bower.which') as which:
			which.return_value = '/discovered/path'
			assert_equal(bower.get_bower_executable_path(), '/discovered/path')


def test_bower_get_rc_file():
	"""Tests that the .bowerrc file is discoverable and usable as a JSON object"""
	with override_settings(BOWER_RC_FILE='/path/to/rc'):
		assert_equal(bower.get_bower_rc_path(), '/path/to/rc')

	with override_settings():
		assert_equal(bower.get_bower_rc_path(), os.getcwd() + '/.bowerrc')


def test_bower_get_component_path():
	"""Tests that the directory bower installs to is discovered correctly"""

	with mock.patch('django_collectstatic_bower.bower.load_bower_rc') as rc:
		rc.return_value = {'directory': '/path/to/components'}

		assert_equal(bower.get_bower_components_path(), '/path/to/components')
