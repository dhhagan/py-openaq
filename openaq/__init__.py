import json
import requests

from pkg_resources import get_distribution
from .exceptions import ApiError

from .decorators import pandasize

__all__ = ['OpenAQ']

__version__ = get_distribution('py-openaq').version

class API(object):
    """Generic API wrapper object.
    """
    def __init__(self, **kwargs):
        self._key       = kwargs.pop('key', '')
        self._pswd      = kwargs.pop('pswd', '')
        self._version   = kwargs.pop('version', None)
        self._baseurl   = kwargs.pop('baseurl', None)
        self._headers   = {'content-type': 'application/json'}

    def _make_url(self, endpoint, **kwargs):
        """Internal method to create a url from an endpoint.

        :param endpoint: Endpoint for an API call

        :type endpoint: string

        :returns: url
        """
        endpoint = "{}/{}/{}".format(self._baseurl, self._version, endpoint)

        extra = []
        for key, value in kwargs.items():
            if isinstance(value, list):
                value = ','.join(value)
            extra.append("{}={}".format(key, value))

        if len(extra) > 0:
            endpoint = '?'.join([endpoint, '&'.join(extra)])

        return endpoint

    def _send(self, endpoint, method = 'GET', data = None, **kwargs):
        """Make an API call of any method

        :param endpoint: API endpoint
        :param method: API call type. Options are PUT, POST, GET, DELETE
        :param data: data to send for POST and PUT calls

        :type endpoint: string
        :type method: string
        :type data: dictionary

        :returns: (status_code, json_response)

        :raises ApiError: raises an exception
        """
        auth = (self._key, self._pswd)
        url  = self._make_url(endpoint, **kwargs)

        if data:
            data = json.dumps(data)

        if method == 'GET':
            try:
                resp = requests.get(url, auth = auth, headers = self._headers)
            except Exception as error:
                raise ApiError(error)
        else:
            raise ApiError("Invalid Method")

        return resp.status_code, resp.json()

    def _get(self, url, **kwargs):
        return self._send(url, 'GET', **kwargs)

class OpenAQ(API):
    """Create an instance of the OpenAQ API

    :param version: API version.
    :param kwargs: API options.

    :type version: string
    """
    def __init__(self, version = 'v1', **kwargs):
        self._baseurl = 'https://api.openaq.org'

        super(OpenAQ, self).__init__(version = version, baseurl = self._baseurl)

    @pandasize()
    def cities(self, **kwargs):
        """Returns a listing of cities within the platform.

        :param country: limit results by a certain country
        :param df: convert the output from json to a pandas DataFrame

        :return: dictionary containing the *city*, *country*, *count*, and number of *locations*

        :type country: 2-digit ISO code
        :type df: boolean

        :Example:

        >>> import openaq
        >>> api = openaq.OpenAQ()
        >>> status, resp = api.cities()
        >>> resp
        [
            {
                "city": "Amsterdam",
                "country": "NL",
                "count": 21301,
                "locations": 14
            },
            {
                "city": "Badhoevedorp",
                "country": "NL",
                "count": 2326,
                "locations": 1
            },
            ...
        ]
        """
        return self._get('cities', **kwargs)

    @pandasize()
    def countries(self, **kwargs):
        """Returns a listing of all countries within the platform

        :param df: return the results as a pandas DataFrame

        :type df: boolean

        :return: dictionary containing the *code*, *name*, and *count*

        :Example:

        >>> import openaq
        >>> api = openaq.OpenAQ()
        >>> status, resp = api.countries()
        >>> resp
        [
            {
                "count": 40638,
                "code": "AU",
                "name": "Australia"
            },
            {
                "count": 78681,
                "code": "BR",
                "name": "Brazil",
            },
            ...
        ]
        """
        return self._get('countries', **kwargs)

    @pandasize()
    def latest(self, **kwargs):
        """Provides the latest value of each parameter for each location

        :param city: limit results by a certain city. Defaults to ``None``.
        :param country: limit results by a certain country. Should be a 2-digit
                        ISO country code. Defaults to ``None``.
        :param location: limit results by a city. Defaults to ``None``.
        :param parameter: limit results by a specific parameter. Options include [
                            pm25, pm10, so2, co, no2, o3, bc]
        :param has_geo: filter items that do or do not have geographic information.
        :param df: return results as a pandas DataFrame

        :type city: string
        :type country: string
        :type location: string
        :type parameter: string
        :type has_geo: boolean
        :type df: boolean

        :return: dictionary containing the *location*, *country*, *city*, and number of *measurements*

        :Example:

        >>> import openaq
        >>> api = openaq.OpenAQ()
        >>> status, resp = api.latest()
        >>> resp
        [
            {
                "location": "Punjabi Bagh",
                "city": "Delhi",
                "country": "IN",
                "measurements": [
                    {
                        "parameter": "so2",
                        "value": 7.8,
                        "unit": "ug/m3",
                        "lastUpdated": "2015-07-24T11:30:00.000Z"
                    },
                    {
                        "parameter": "co",
                        "value": 1.3,
                        "unit": "mg/m3",
                        "lastUpdated": "2015-07-24T11:30:00.000Z"
                    },
                    ...
                ]
                ...
            }
        ]
        """
        return self._get('latest', **kwargs)

    @pandasize()
    def locations(self, **kwargs):
        """Provides metadata about distinct measurement locations

        :param city: Limit results by a certain city. Defaults to ``None``.
        :param country: Limit results by a certain country. Should be a 2-digit
                        ISO country code. Defaults to ``None``.
        :param location: Limit results by a city. Defaults to ``None``.
        :param parameter: Limit results by a specific parameter. Options include [
                            pm25, pm10, so2, co, no2, o3, bc]
        :param has_geo: Filter items that do or do not have geographic information.

        :type city: string
        :type country: string
        :type location: string
        :type parameter: string
        :type has_geo: boolean

        :return: a dictionary containing the *loction*, *country*, *city*, *count*,
                    *sourceName*, *firstUpdated*, *lastUpdated*, *parameters*, and *coordinates*

        :Example:

        >>> import openaq
        >>> api = openaq.OpenAQ()
        >>> status, resp = api.locations()
        >>> resp
        [
            {
                "count": 4242,
                "sourceName": "Australia - New South Wales",
                "firstUpdated": "2015-07-24T11:30:00.000Z",
                "lastUpdated": "2015-07-24T11:30:00.000Z",
                "parameters": [
                    "pm25",
                    "pm10",
                    "so2",
                    "co",
                    "no2",
                    "o3"
                ],
                "country": "AU",
                "city": "Central Coast",
                "location": "wyong"
            },
            ...
        ]
        """
        return self._get('locations', **kwargs)

    @pandasize()
    def measurements(self, **kwargs):
        """Provides metadata about distinct measurement locations

        :param city: Limit results by a certain city. Defaults to ``None``.
        :param country: Limit results by a certain country. Should be a 2-digit
                        ISO country code. Defaults to ``None``.
        :param location: Limit results by a city. Defaults to ``None``.
        :param parameter: Limit results by a specific parameter. Options include [
                            pm25, pm10, so2, co, no2, o3, bc]
        :param has_geo: Filter items that do or do not have geographic information.
        :param value_from: Show results above a value threshold.
        :param value_to: Show results below a value threshold.
        :param date_from: Show results after a certain date. Format should be ``Y-M-D``
        :param date_to: Show results before a certain date. Format should be ``Y-M-D``
        :param sort: The sort order (``asc`` or ``desc``).
        :param order_by: Field to sort by. Must be used with **sort**.
        :param include_fields: Include additional fields in the output.
        :param limit: Change the number of results returned.
        :param page: Paginate through the results
        :param skip: Number of records to skip.
        :param df: return the results as a pandas DataFrame

        :type city: string
        :type country: string
        :type location: string
        :type parameter: string
        :type has_geo: boolean
        :type value_from: number
        :type value_to: number
        :type date_from: date
        :type date_to: date
        :type sort: string
        :type order_by: string
        :type include_fields: array
        :type limit: number
        :type page: number
        :type skip: number
        :type df: boolean

        :return: a dictionary containing the *date*, *parameter*, *value*, *unit*,
            *location*, *country*, *city*, and *coordinates*.

        :Example:

        >>> import openaq
        >>> api = openaq.OpenAQ()
        >>> status, resp = api.measurements(city = 'Delhi')
        >>> resp
        {
            "parameter": "Ammonia",
            "date": {
                "utc": "2015-07-16T20:30:00.000Z",
                'local': "2015-07-16T18:30:00.000-02:00"
            },
            "value": "72.9",
            "unit": "ug/m3",
            "location": "Anand Vihar",
            "country": "IN",
            "city": "Delhi",
            "coordinates": {
                "latitude": 43.34,
                "longitude": 23.04
            },
            ...
        }
        """
        return self._get('measurements', **kwargs)

    def fetches(self, **kwargs):
        """Provides data about individual fetch operations that are used to populate
        data in the platform.

        :return: dictionary containing the *timeStarted*, *timeEnded*, *count*, and *results*

        :Example:

        >>> import openaq
        >>> api = openaq.OpenAQ()
        >>> status, resp = api.fetches()
        >>> resp
        {
            "meta": {
                "name": "openaq-api",
                "license":
                "website":
                "page": 1,
                "limit": 100,
                "found": 3
            },
            "results": [
                {
                    "count": 0,
                    "results": [
                        {
                            "message": "New measurements inserted for Mandir Marg: 1",
                            "failures": {},
                            "count": 0,
                            "duration": 0.153,
                            "sourceName": "Mandir Marg"
                        },
                        {
                            "message": "New measurements inserted for Sao Paulo: 1898",
                            "failures": {},
                            "count": 1898,
                            "duration": 16.918,
                            "sourceName": "Sao Paulo"
                        },
                        ...
                    ],
                    "timeStarted": "2016-02-07T15:25:04.603Z",
                    "timeEnded": "2016-02-07T15:25:04.793Z",
                }
            ]
        }
        """
        return self._get('fetches', **kwargs)

    def __repr__(self):
        return "OpenAQ API"
