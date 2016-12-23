import unittest
import openaq
import pandas as pd
from openaq.viz import *

class SetupTestCase(unittest.TestCase):
    def setUp(self):
        self.api = openaq.OpenAQ()

    def tearDown(self):
        pass

    def test_setup(self):
        self.assertIsInstance(self.api, openaq.OpenAQ)

    def test_tsplot_1hr(self):
        data = self.api.measurements(
                    city = 'Delhi',
                    parameter = 'pm25',
                    location = 'Anand Vihar',
                    limit = 5,
                    df = True)

        a = tsplot(data)

    def test_tsplot_24hr(self):
        data = self.api.measurements(
                    country = 'IN',
                    city = 'Delhi',
                    location = 'Anand Vihar',
                    parameter = 'pm25',
                    limit = 20,
                    index = 'local',
                    df = True)

        a = tsplot(data)

    def test_tsplot_1wk(self):
        data = self.api.measurements(
                    country = 'IN',
                    city = 'Delhi',
                    location = 'Anand Vihar',
                    parameter = 'pm25',
                    limit = 100,
                    index = 'local',
                    df = True)

        a = tsplot(data)

    def test_tsplot_2wk(self):
        data = self.api.measurements(
                    country = 'IN',
                    city = 'Delhi',
                    location = 'Anand Vihar',
                    parameter = 'pm25',
                    limit = 400,
                    index = 'local',
                    df = True)

        a = tsplot(data)

    def test_tsplot_4wk(self):
        data = self.api.measurements(
                    country = 'IN',
                    city = 'Delhi',
                    location = 'Anand Vihar',
                    parameter = 'pm25',
                    limit = 600,
                    index = 'local',
                    df = True)

        a = tsplot(data)

    def test_tsplot_1month(self):
        data = self.api.measurements(
                    country = 'IN',
                    city = 'Delhi',
                    location = 'Anand Vihar',
                    parameter = 'pm25',
                    limit = 900,
                    index = 'local',
                    df = True)

        a = tsplot(data)

    def test_tsplot_1yr(self):
        data = self.api.measurements(
                    country = 'IN',
                    city = 'Delhi',
                    location = 'Anand Vihar',
                    parameter = 'pm25',
                    limit = 1500,
                    index = 'local',
                    df = True)

        a = tsplot(data)

        self.assertIsNotNone(a)

    def test_tsplot_1yr(self):
        data = self.api.measurements(
                    country = 'IN',
                    city = 'Delhi',
                    location = 'Anand Vihar',
                    parameter = 'pm25',
                    limit = 10000,
                    index = 'local',
                    df = True)

        a = tsplot(data)
