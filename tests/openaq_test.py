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
        status, resp = self.api.cities()

        self.assertTrue(status == 200)

    def test_countries(self):
        pass

    def test_latest(self):
        pass

    def test_locations(self):
        pass

    def test_measurements(self):
        pass

    def test_failed_call(self):
        pass

if __name__ == '__main__':
    unittest.main()
