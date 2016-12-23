.. py-openaq documentation master file, created by
   sphinx-quickstart on Sat Dec 26 08:07:34 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


Welcome to py-openaq's documentation!
=====================================

**py-openaq** provides easy access to the Open AQ API.

Installation
------------
You can install this package in the usual way using ``pip``::

    pip install py-openaq

You can upgrade this package using ``pip`` as well::

    pip install py-openaq --upgrade


Requirements
------------

The only requirement for this package is ``requests``. If you are not limited
by memory or space, I would highly recommend installing ``pandas`` and ``seaborn``
which will enable you to use the new visualization helpers that were released with
version 1.

Current Limitations
-------------------
As of now, the only feature that is not built into the API wrapper is returning various formats
from the ``openaq.OpenAQ.measurements`` call. This is because I don't see any reason to use python
to return a csv. If a csv is your desired output, I recommend using pandas' ``DataFrame.to_csv()`` method.

Initialization
--------------

The following code example shows how to make your first API call::

    import openaq

    api = openaq.OpenAQ()

    status, resp = api.cities()

Understanding the Response format
---------------------------------

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
------------------------------
The `pandasize` decorator was added to easily allow you to read in data directly
to a DataFrame. To do so, simply add the argument `df = True` to your request.

The following API methods allow you to return your data as a DataFrame:

  * cities
  * countries
  * latest
  * locations
  * measurements
  * sources

By using this keyword argument, the results of the API call will return a pandas DataFrame rather than a json response.

Example:

    >>> df = api.latest(df = True)

The results are parsed through the `pandasize` decorator which tries to interpret the fields in the most ideal format possible.
Thus, all datetime fields should be converted to proper python datetimes to allow for easy splicing, manipulation, and plotting.

API Reference
=============

.. module:: openaq
.. autoclass:: OpenAQ
   :members: cities, countries, latest, locations, measurements, fetches,
                parameters, sources
