import json
import os
import shutil

import subprocess
from django.conf import settings


def get_bower_executable_path():
	"""Find bower executable"""
	return getattr(settings, 'BOWER_CMD', shutil.which('bower'))

def get_bower_rc_path():
	"""Find .bowerrc file"""
	return getattr(settings, 'BOWER_RC_FILE', os.path.join(
		os.getcwd(),
		'.bowerrc'
	))

def get_bower_json_path():
	"""Find bower.json file"""
	return getattr(settings, 'BOWER_JSON_FILE', os.path.join(
		os.getcwd(),
		'bower.json'
	))

def get_bower_components_path():
	"""Returns bower components path"""
	rc = load_bower_rc()

	if rc:
		path = os.path.abspath(rc.get('directory', 'bower_components/'))
	else:
		path = os.path.join(
			os.getcwd(),
			'bower_components/'
		)

	return os.path.abspath(path)

def load_bower_rc():
	"""Returns parsed .bowerrc file"""
	try:
		with open(get_bower_rc_path()) as rc:
			return json.load(rc)
	except Exception:
		return None

def load_bower_json():
	"""Returns parsed bower.json file"""
	try:
		with open(get_bower_json_path()) as bower_json:
			return json.load(bower_json)
	except Exception:
		return None

def bower(*args, cwd=None):
	"""Runs bower with provided args"""
	cwd = cwd or os.getcwd()

	proc = subprocess.Popen(
		(get_bower_executable_path(),) + args,
		cwd=cwd
	)
	proc.wait()

	if proc.returncode:
		raise RuntimeError('Bower command failed')

	return proc
