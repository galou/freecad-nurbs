"""Provides reload_module."""

import sys


def reload_module(module):
	if sys.version_info.major > 2:
		import importlib
		importlib.reload(module)
	else:
		reload(module)
