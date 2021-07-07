import unittest
import openaq
import pandas as pd

class SetupTestCase(unittest.TestCase):
    def setUp(self):
        self.api = openaq.OpenAQ()

    def tearDown(self):
        pass

    def test_setup(self):
        self.assertIsInstance(self.api, openaq.OpenAQ)

    def test_incorrect_api_method(self):
        with self.assertRaises(openaq.exceptions.ApiError):
            res = self.api._send('cities', method = 'BAD')

    def test_cities(self):
        status, resp = self.api.cities(
                        country = 'US'
                        )

        self.assertTrue(status == 200)

        # Test order_by
        status, resp = self.api.cities(country='US', order_by='country')
        self.assertTrue(status == 200)

        status, resp = self.api.cities(country='US', order_by=['country', 'city'])
        self.assertTrue(status == 200)

        # Test sorting
        status, resp = self.api.cities(country='US', sort='asc')
        self.assertTrue(status == 200)

    def test_add_pages(self):
        status, resp = self.api.cities( country = 'US' )

        self.assertIsNotNone(resp['meta']['pages'])

    def test_countries(self):
        status, resp = self.api.countries()

        self.assertTrue(status == 200)

    def test_latest(self):
        status, resp = self.api.latest(
            city = 'Delhi',
            country = 'IN',
            location = 'Punjabi Bagh'
        )

        self.assertTrue(status == 200)

    def test_locations(self):
        status, resp = self.api.locations(city = 'Delhi')

        self.assertTrue(status == 200)

    def test_locations_with_params(self):
        # Test cities as a list
        status, resp = self.api.locations(
            city = ['Delhi', 'Mumbai']
            )

        for r in resp['results']:
            self.assertTrue(r['city'] in ['Delhi', 'Mumbai'])

        # Test cities as a tuple
        status, resp = self.api.locations(
            city = ('Delhi', 'Mumbai')
        )

        for r in resp['results']:
            self.assertTrue(r['city'] in ['Delhi', 'Mumbai'])

    def test_measurements(self):
        status, resp = self.api.measurements(city='Delhi')

        self.assertTrue(status == 200)

    def test_pandasize(self):
        resp    = self.api.latest(df=True)
        resp2   = self.api.measurements(df=True)
        resp3   = self.api.measurements(df=True, index='utc')
        resp4   = self.api.measurements(df=True, index=None)

        self.assertIsInstance(resp, pd.DataFrame)
        self.assertIsInstance(resp2, pd.DataFrame)
        self.assertIsInstance(resp3, pd.DataFrame)
        self.assertIsInstance(resp4, pd.DataFrame)

        # make sure the index for resp4 are ints
        self.assertTrue(type(resp4.index.values[0]), int)

    def test_fetches(self):
        status, resp = self.api.fetches()

        self.assertTrue(status == 200)

    def test_bad_request(self):
        endpoint = "http://api.openaq.org/v1/fetch"

        with self.assertRaises(openaq.exceptions.ApiError):
            status, resp = self.api._send('PUT')

    def test_parameters(self):
        status, resp = self.api.parameters()

        self.assertIsNotNone(resp['results'])

    def test_sources(self):
        status, resp = self.api.sources(limit=1)

        self.assertIsNotNone(resp['results'])

    def test_local_time(self):
        status, resp = self.api.measurements(city='Hilo')

        self.assertTrue(status == 200)

        # Make sure that the localtime and utc time are 10 hours different

    def test_repr(self):
        self.assertTrue(str(self.api) == 'OpenAQ API')


if __name__ == '__main__':
    unittest.main()
