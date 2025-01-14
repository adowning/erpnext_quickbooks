
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from setuptools import setup, find_packages
import re, ast

# get version from __version__ variable in erpnext/__init__.py
# _version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

version = '0.0.1'


setup(
	name='erpnext_quickbooks',
	version=version,
	description='Quickbooks connector for ERPNext',
	author='Frappe Technologies Pvt. Ltd.',
	author_email='info@frappe.io',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
