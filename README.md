[![Build Status](https://travis-ci.org/dhhagan/py-openaq.svg?branch=master)](https://travis-ci.org/dhhagan/py-openaq)

[![Coverage Status](https://coveralls.io/repos/dhhagan/py-openaq/badge.svg?branch=master&service=github)](https://coveralls.io/github/dhhagan/py-openaq?branch=master)

# py-openaq
This project contains the python wrapper for the [Open AQ API](https://docs.openaq.org/).


## Installation

    pip install py-openaq

### Git
    >>> git clone https://github.com/dhhagan/py-openaq.git
    >>> cd /py-openaq
    >>> python3 setup.py install

### wget

    >>> wget https://github.com/dhhagan/py-openaq.git
    >>> unzip py-openaq.zip
    >>> cd /py-openaq
    >>> python3 setup.py install

### Upgrade to newer release (from git repo)

    >>> git pull
    >>> cd /py-openaq
    >>> python3 setup.py install --force

## API

Most of the syntax is copied directly from the [API docs](https://docs.openaq.org/).
For a (much) more detailed look at the API calls, take a look at the Jupyter Notebook!

All methods return a tuple containing `(status_code, response)`

### Settings

    api = openaq.OpenAQ()

    ...

| parameter | type | default | options | comments |
|:----------|:----:|:-------:|:--------|:--------:|
| version | string | 'v1' || |
| **kwargs | dict | | | Not used as of now |

### Methods

#### cities

Provides a listing of cities within the platform

    api.cities()

| parameter | type | default | example |
|:----------|:----:|:-------:|:--------|
| country | string | None | 'US' |

#### countries

Provides a listing of countries within the platform

    api.countries()

#### latest

Provides the latest parameter for every available location in the platform

    api.latest()

| parameter | type | default | example |
|:----------|:----:|:-------:|:--------|
| city | string | None | 'Delhi' |
| country | string | None | 'IN' |
| location | string | None | 'Punjabi Bagh' |
| parameter | string | None | 'pm25' |
| has_geo | boolean | None | True |
| value_from | number | None | 100 |
| value_to | number | None | 200 |

#### locations

Provides metadata for distinct measurement locations

    api.locations()

*NOTE: Dates are in the format YYYY-MM-DD*

| parameter | type | default | example |
|:----------|:----:|:-------:|:--------|
| city | string | None | 'Delhi' |
| country | string | None | 'IN' |
| location | string | None | 'Punjabi Bagh' |
| parameter | string | None | 'pm25' |
| has_geo | boolean | None | True |
| value_from | number | None | 100 |
| value_to | number | None | 200 |
| date_from | date | None | '2015-01-01 |
| date_to | date | None | '2015-12-20 |

#### measurements

Provides data about individual measurements

    api.measurements()

*NOTE: Dates are in the format YYYY-MM-DD*

| parameter | type | default | example |
|:----------|:----:|:-------:|:--------|
| city | string | None | 'Delhi' |
| country | string | None | 'IN' |
| location | string | None | 'Punjabi Bagh' |
| parameter | string | None | 'pm25' |
| has_geo | boolean | None | True |
| value_from | number | None | 100 |
| value_to | number | None | 200 |
| date_from | date | None | '2015-01-01' |
| date_to | date | None | '2015-12-20' |
| sort | string | None | 'asc' |
| order_by | string | None | 'city' |
| include_fields | array | None | ['location', 'parameter'] |
| limit | number | None | 100 |
| page | number | None | 2 |
| skip | number | None | 500 |
