'''
	Python wrapper for the OpenAQ API
	Written originally by David H Hagan
	December 2015
'''
__version__ = '0.1.3'

try:
	from setuptools import setup
except:
	from distutils.core import setup

setup(
	name = 'py-openaq',
	version = __version__,
	description = 'Python wrapper for the OpenAQ API',
	keywords = ['OpenAQ', 'MIT', 'Air Quality'],
	author = 'David H Hagan',
	author_email = 'david@davidhhagan.com',
	url = 'https://github.com/dhhagan/py-openaq',
	license = 'MIT',
	packages = ['openaq'],
	classifiers = [
		'Development Status :: 1 - alpha',
		'Operating System :: OS Independent',
		'Intended Audience :: Science/Research',
		'Programming Language :: Python :: 3',
		'Topic :: Software Development',
		'Topic :: System :: Software',
		'Topic :: API',
		'Topic :: Software Development :: Libraries :: Python Modules'
	]
)
