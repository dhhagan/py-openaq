#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dateutil

def to_naive_timestamp(timestamp):
    """
        Convert a timezone aware timestamp (as a string) and return the
        python datetime in the local timezone, but without the tzinfo attribute
    """
    return dateutil.parser.parse(timestamp).replace(tzinfo=None).isoformat()

def clean_encodings(unit):
    if unit not in ('ppm', 'ppb', 'ppt', 'ugm3'):
        unit = unit.encode('utf-8')

        if unit == '\xc2\xb5g/m\xc2\xb3':
            unit = 'ugm3'

    return unit

def mass_to_mix(value, param, unit='ppb', **kwargs):
    """Convert units from ug/m3 to ppb or ppm. The conversion assumes an ambient
    pressure of 1 atmosphere and ambient temperature of 25 degC.

    :param value: the concentration in ug/m3
    :param param: the parameter to convert {'co', 'no', 'no2', 'so2', 'o3'}
    :param unit: the desired output unit {'ppb', 'ppm'}

    :type value: float
    :type param: string
    :type unit: string

    :returns: value

    :Example:

    >>> import openaq
    >>> conc_ugm3 = 100
    >>> conc_ppb = openaq.utils.mass_to_mix(conc_ugm3, param='co', unit='ppb')
    >>> conc_ppb
    114.5

    """
    lookup = {
        'co': 1.145,
        'no': 1.25,
        'no2': 1.88,
        'so2': 2.62,
        'o3': 2.0
    }

    param = param.lower()

    if param not in lookup.keys():
        return value

    value = value / lookup[param]

    if unit.lower() == 'ppm':
        value *= 1e-3

    return value
