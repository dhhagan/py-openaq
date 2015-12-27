[![Build Status](https://travis-ci.org/dhhagan/py-openaq.svg?branch=master)](https://travis-ci.org/dhhagan/py-openaq)
[![Coverage Status](https://coveralls.io/repos/dhhagan/py-openaq/badge.svg?branch=master&service=github)](https://coveralls.io/github/dhhagan/py-openaq?branch=master)

# py-openaq
This project contains the python wrapper for the [Open AQ API](https://docs.openaq.org/).

Full documentation can be found [here](http://py-openaq.readthedocs.org/en/latest/)!



## Installation

    pip install py-openaq

## Quickstart

    import openaq

    api = openaq.OpenAQ()

    status, resp = api.cities()
