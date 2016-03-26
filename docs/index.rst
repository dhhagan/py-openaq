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


Requirements
------------

The only requirement for this package is ``requests``. In the future (v1),
``pandas`` will be recommended and significant features will depend on it.

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
Pandas is awesome. If you are working with data, you should be using DataFrames. To
easily dump your json response into a DataFrame::

    from pandas.io.json import json_normalize

    df = json_normalize(resp)


API Reference
=============

.. module:: openaq
.. autoclass:: OpenAQ
   :members: cities, countries, latest, locations, measurements, fetches
