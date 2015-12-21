# py-openaq
Python wrapper for the Open AQ API

For documentation on the API, please see https://docs.openaq.org/

## Installation

    >>> git clone https://github.com/dhhagan/py-openaq.git
    >>> cd /py-openaq
    >>> python3 setup.py install

  - OR -

    >>> wget https://github.com/dhhagan/py-openaq.git
    >>> unzip py-openaq.zip
    >>> cd /py-openaq
    >>> python3 setup.py install

### Upgrade to newer distribution (from git repo)

    >>> git pull
    >>> cd /py-openaq
    >>> python3 setup.py install --force

## Usage

Most of the syntax is copied directly from the [API docs](https://docs.openaq.org/).
For a (much) more detailed look at the API calls, take a look at the Jupyter Notebook!

    >>> from openaq import OpenAQ
    >>> api = OpenAQ()
    >>> status, resp = api.cities()

## API
