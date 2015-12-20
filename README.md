# py-openaq
Python wrapper for the Open AQ API

For documentation on the API, please see https://docs.openaq.org/

## Installation

    >>> git clone https://github.com/dhhagan/py-openaq.git
    >>> cd /py-openaq
    >>> python setup.py install

## Usage

    >>> from openaq import OpenAQ
    >>> api = OpenAQ()
    >>> status, resp = api.cities()
