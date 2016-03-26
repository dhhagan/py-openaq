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

    def test_cities(self):
        status, resp = self.api.cities(
                        country = 'US'
                        )

        self.assertTrue(status == 200)

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

    def test_measurements(self):
        status, resp = self.api.measurements(city = 'Delhi')

        self.assertTrue(status == 200)

    def test_measurements_with_params(self):
        status, resp = self.api.measurements(include_fields = ['location', 'parameter',
                                'date', 'value'])

        self.assertTrue(status == 200)

    def test_pandasize(self):
        resp    = self.api.latest(df = True)
        resp2   = self.api.measurements(df = True)
        resp3   = self.api.measurements(df = True, index = 'utc')

        self.assertTrue(type(resp) == pd.DataFrame)
        self.assertTrue(type(resp) == pd.DataFrame)

    def test_fetches(self):
        status, resp = self.api.fetches()

        self.assertTrue(status == 200)

    def test_bad_request(self):
        endpoint = "http://api.openaq.org/v1/fetch"

        status, resp = self.api._send('PUT')

        self.assertRaises(openaq.exceptions.ApiError)

    def test_repr(self):
        self.assertTrue(str(self.api) == 'OpenAQ API')


if __name__ == '__main__':
    unittest.main()
