#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import wraps
import warnings
from unittest import SkipTest
from .utils import to_naive_timestamp, clean_encodings

try:
    import pandas as pd

    _no_pandas = False
except ImportError:
    _no_pandas = True

def skipif(skipcondition, msg = ""):
    """
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if skipcondition == True:
                raise SkipTest(msg)

            return f(*args, **kwargs)
        return decorated_function
    return  decorator

def pandasize():
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            df = kwargs.pop('df', False)
            index = kwargs.pop('index', 'local')

            if df == True and _no_pandas == False:
                status, resp = f(*args, **kwargs)

                if status == 200:
                    resp = resp['results']

                    # Empty DataFrame when no results are returned
                    if not resp:
                        return pd.DataFrame(
                            columns= ['date.local', 'city', 
                                'coordinates.latitude', 'coordinates.longitude', 
                                'country', 'date.utc', 'location', 
                                'parameter', 'unit', 'value']).set_index('date.local')

                    if f.__name__ == 'latest':
                        d = []
                        for i in resp:
                            for m in i['measurements']:
                                tmp = m
                                tmp['country'] = i['country']
                                tmp['city'] = i['city']
                                tmp['location'] = i['location']

                                tmp['lastUpdated'] = pd.to_datetime(tmp['lastUpdated'])

                                d.append(tmp)

                            resp = d

                    data = pd.io.json.json_normalize(resp)

                    # If there are any datetimes, make them datetimes!
                    for each in [i for i in data.columns if 'date' in i]:
                        if 'local' in each:
                            data[each] = pd.to_datetime(data[each].apply(lambda x: to_naive_timestamp(x)))
                        else:
                            data[each] = pd.to_datetime(data[each])

                    if f.__name__ in ('latest'):
                        data.index = data['lastUpdated']

                        del data['lastUpdated']

                    elif f.__name__ in ('measurements'):
                        if index == 'utc':
                            data.index = data['date.utc']
                            del data['date.utc']
                        elif index == 'local':
                            data.index = data['date.local']
                            del data['date.local']
                        else:
                            pass

                    # Clean up encodings
                    if 'unit' in data.columns:
                        data['unit'] = data['unit'].apply(clean_encodings)

                    return data

            return f(*args, **kwargs)
        return decorated_function
    return decorator
