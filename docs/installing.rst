.. _installing:

Getting Started and Installation
--------------------------------

``py-openaq`` aims to provide easy access to the OpenAQ API via a Python
platform. To read more about OpenAQ, check out their `website <https://openaq.org>`_.


Installation
============

You can install the package directly via pypi through ``pip``:

``>>> pip install py-openaq``

You can also install the most up-to-date development version directly from github
using:

``>>> pip install git+https://github.com/dhhagan/py-openaq.git``

Requirements
============

Mandatory
~~~~~~~~~

+ Python2.7 or Python3.3+
+ `requests <http://docs.python-requests.org/en/master/>`_

Recommended
~~~~~~~~~~~

+ `pandas <http://pandas.pydata.org/>`_
+ `seaborn <http://seaborn.pydata.org/index.html>`_
+ `matplotlib <http://matplotlib.org>`_

Current Limitations
===================
As of now, the only feature that is not built into the API wrapper is returning various formats
from the ``openaq.OpenAQ.measurements`` call. This is because I don't see any reason to use python
to return a csv. If a csv is your desired output, I recommend using pandas' ``DataFrame.to_csv()`` method.

Initialization
==============

The following code example shows how to make your first API call::

    import openaq

    api = openaq.OpenAQ()

    status, resp = api.cities()

Understanding the Response format
=================================

Each API call will reply with a tuple containing the status code and the response
in json format. The three most common API status codes you will see are:

  * 200: Success
  * 40x: Error: Bad Request
  * 500: Server Error

The json response will look something like the following with both ``meta`` and ``results``::

    {
    'meta': {'license': 'CC By 4.0', 'name': 'openaq-api', 'website': 'https://docs.openaq.org/'},
    'results': [
        {'city': 'Amsterdam', 'count': 71125, 'country': 'NL', 'locations': 14},
        {'city': 'Antofagasta', 'count': 3416, 'country': 'CL', 'locations': 1},
        {'city': 'Arica', 'count': 1682, 'country': 'CL', 'locations': 1},
        {'city': 'Ayutthaya', 'count': 3880, 'country': 'TH', 'locations': 1},
        {'city': 'Badhoevedorp', 'count': 7862, 'country': 'NL', 'locations': 1},
        ...
        ]
    }


Coupling with Pandas DataFrame
==============================
Pandas is awesome. If you are working with data, you should be using DataFrames. To
easily dump your json response into a DataFrame::

    from pandas.io.json import json_normalize

    df = json_normalize(resp)

As of v0.3.0, an optional keyword argument (`df`) has been added to the following API methods:

  * cities
  * countries
  * latest
  * locations
  * measurements

By using this keyword argument, the results of the API call will return a pandas DataFrame rather than a json response.

Example:

    >>> df = api.latest(df=True)

The results are parsed through the `pandasize` decorator which tries to interpret the fields in the most ideal format possible.
Thus, all datetime fields should be converted to proper python datetimes to allow for easy splicing, manipulation, and plotting.


Testing
=======

Testing is automated using unittests. To run the unittests with coverage
reporting, run the following command from the main directory:

``>>> coverage run --source openaq setup.py test``

You can then view the coverage report with:

``>>> coverage report -m``

Bugs and Issues
===============

Please report any bugs or issues you find through the `GitHub issues tracker
<https://github.com/dhhagan/py-openaq/issues/new>`_. Please provide as much
information as possible that will make it easier to solve/fix the problem.
