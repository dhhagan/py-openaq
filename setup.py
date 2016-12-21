'''
	Python wrapper for the OpenAQ API
	Written originally by David H Hagan
	December 2015
'''
__version__ = '1.0.0'

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
	test_suite = 'tests',
	classifiers = [
		'Development Status :: 3 - Alpha',
		'Operating System :: OS Independent',
		'Intended Audience :: Science/Research',
		'Intended Audience :: Developers',
		'Intended Audience :: Education',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3.3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Topic :: Scientific/Engineering :: Atmospheric Science',
		'Topic :: Software Development',
		'Topic :: Software Development :: Libraries :: Python Modules'
	]
)
