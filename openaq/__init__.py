import json
import requests

from pkg_resources import get_distribution
from .exceptions import ApiError

__all__ = ['OpenAQ']

__version__ = get_distribution('py-openaq').version

class API(object):
    def __init__(self, **kwargs):
        self._key       = kwargs.pop('key', '')
        self._pswd      = kwargs.pop('pswd', '')
        self._version   = kwargs.pop('version', None)
        self._baseurl   = kwargs.pop('baseurl', None)
        self._headers   = {'content-type': 'application/json'}

    def _make_url(self, endpoint, **kwargs):
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
        ''' '''
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
    """
    def __init__(self, version = 'v1', **kwargs):
        self._baseurl = 'https://api.openaq.org'

        super(OpenAQ, self).__init__(version = version, baseurl = self._baseurl)

    def cities(self, **kwargs):
        """Returns a listing of cities within the platform.

        :param country: Limit results by a certain country. Expects
                        a 2-digit ISO code.

        :type country: string
        """
        return self._get('cities', **kwargs)

    def countries(self, **kwargs):
        """Provides a listing of all countries within the platform
        """
        return self._get('countries', **kwargs)

    def latest(self, **kwargs):
        """Provides the latest value of each parameter for each location

        :param city: Limit results by a certain city. Defaults to ``None``.
        :param country: Limit results by a certain country. Should be a 2-digit
                        ISO country code. Defaults to ``None``.
        :param location: Limit results by a city. Defaults to ``None``.
        :param parameter: Limit results by a specific parameter. Options include [
                            pm25, pm10, so2, co, no2, o3, bc]
        :param has_geo: Filter items that do or do not have geographic information.
        :param value_from: Show results above a value threshold.
        :param value_to: Show results below a value threshold.

        :type city: string
        :type country: string
        :type location: string
        :type parameter: string
        :type has_geo: boolean
        :type value_from: number
        :type value_to: number
        """
        return self._get('latest', **kwargs)

    def locations(self, **kwargs):
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

        :type city: string
        :type country: string
        :type location: string
        :type parameter: string
        :type has_geo: boolean
        :type value_from: number
        :type value_to: number
        :type date_from: date
        :type date_to: date
        """
        return self._get('locations', **kwargs)

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
        """
        return self._get('measurements', **kwargs)

    def __repr__(self):
        return "OpenAQ API"
