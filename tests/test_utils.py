import unittest
import openaq
import pandas as pd
from openaq.utils import mass_to_mix


class SetupTestCase(unittest.TestCase):
    def setUp(self):
        self.api = openaq.OpenAQ()

    def tearDown(self):
        pass

    def test_mass_to_mix(self):
        mix = mass_to_mix(value=1., param='co', unit='ppb')

        self.assertEqual(mix, 1.145)

        # Test ppm
        mix = mass_to_mix(value=1000., param='co', unit='ppm')

        self.assertEqual(mix, 1.145)

    def test_raise_exception(self):
        with self.assertRaises(Exception):
            val = openaq.utils.mass_to_mix(1, param='h2o2')
