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
        #unit = 'ugm3'
        if unit == '\xc2\xb5g/m\xc2\xb3':
            unit = 'ugm3'

    return unit
