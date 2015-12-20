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
        elif method == 'POST':
            try:
                resp = requests.post(url, auth = auth, headers = self._headers, data = data)
            except Exception as error:
                raise ApiError(error)
        elif method == 'PUT':
            try:
                resp = requests.put(url, auth = auth, headers = self._headers, data = data)
            except Exception as error:
                raise ApiError(error)
        elif method == 'DELETE':
            try:
                resp = requests.delete(url, auth = auth, headers = self._headers)
            except Exception as error:
                raise ApiError(error)
        else:
            return "Invalid Method"

        return resp.status_code, resp.json()

    def _get(self, url, **kwargs):
        return self._send(url, 'GET', **kwargs)

    def _post(self, url, data):
        pass

    def _put(self, url, data):
        pass

    def _delete(self, url):
        pass

class OpenAQ(API):
    ''' Instance of the OpenAQ API as documented here: https://docs.openaq.org/ '''
    def __init__(self, version = 'v1', **kwargs):
        self._baseurl = 'https://api.openaq.org'

        super(OpenAQ, self).__init__(version = version, baseurl = self._baseurl)

    def cities(self, **kwargs):
        '''
            Provides a listing of cities within the platform.
            kwargs include:
                country    string   ex. country='US'
        '''
        return self._get('cities', **kwargs)

    def countries(self, **kwargs):
        '''
            Provides a listing of all countries within the platform
        '''
        return self._get('countries', **kwargs)

    def latest(self, **kwargs):
        '''
            Provides the latest parameter for every available location in the system
            kwargs include:
                city       string   ex. city='Delhi'
                country    string   ex. country='IN'
                location   string   ex. location='Punjabi Bagh'
                parameter  string   ex. parameter='pm25'
                has_geo    boolean  ex. has_geo=True
                value_from number   ex. value_from=100
                value_to   number   ex. value_to=200
        '''
        return self._get('latest', **kwargs)

    def locations(self, **kwargs):
        '''
            Provides metadata for distinct measurement locations
            kwargs inlcude:
                city       string   ex. city='Delhi'
                country    string   ex. country='IN'
                location   string   ex. location='Punjabi Bagh'
                parameter  string   ex. parameter='pm25'
                has_geo    boolean  ex. has_geo=True
                value_from number   ex. value_from=100
                value_to   number   ex. value_to=200
                date_from  string   ex. date_from='2015-01-01' (Y-M-D)
                date_to    string   ex. date_to='2015-12-01'   (Y-M-D)
        '''
        return self._get('locations', **kwargs)

    def measurements(self, **kwargs):
        '''
            Provides data about individual measurements
            kwargs include:
                city            string   ex. city='Delhi'
                country         string   ex. country='IN'
                location        string   ex. location='Punjabi Bagh'
                parameter       string   ex. parameter='pm25'
                has_geo         boolean  ex. has_geo=True
                value_from      number   ex. value_from=100
                value_to        number   ex. value_to=200
                date_from       string   ex. date_from='2015-01-01' (Y-M-D)
                date_to         string   ex. date_to='2015-12-01'   (Y-M-D)
                sort            string   ex. sort='asc'
                order_by        string   ex. order_by='city'
                include_fields  array    ex. include_fields=[location,parameter,date,value]
                limit           number   ex. limit=500
                page            number   ex. page=2
                skip            number   ex. skip=500

            I'm not currently supporting `format` until I figure out how to deal with csv
        '''
        return self._get('measurements', **kwargs)

    def __repr__(self):
        return "OpenAQ APi"
