import unittest
import openaq

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
            location = 'Punjabi Bagh',
            value_from = 200
        )

        self.assertTrue(status == 200)

    def test_locations(self):
        status, resp = self.api.locations(city = 'Delhi')

        self.assertTrue(status == 200)

    def test_measurements(self):
        status, resp = self.api.measurements(city = 'Delhi')

        self.assertTrue(status == 200)

if __name__ == '__main__':
    unittest.main()
