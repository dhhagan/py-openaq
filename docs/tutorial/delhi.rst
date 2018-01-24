
.. _delhi_tutorial:

.. code:: ipython3

    import pandas as pd
    import seaborn as sns
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    import openaq
    import warnings
    
    warnings.simplefilter('ignore')
    
    %matplotlib inline
    
    # Set major seaborn asthetics
    sns.set("notebook", style='ticks', font_scale=1.5)

Evaluating Delhi’s AQ Using OpenAQ
==================================

Most of my own atmospheric chemistry research as a PhD student at MIT is
based in Delhi. Thus, for this tutorial, we will take a deeper look at
the air quality data made available to us through OpenAQ. We will begin
by figuring out exactly what data is available to us, and then further
examine the most relevant and up-to-date sources. We will take a look at
longer trends for some pollutants where possible.

Choosing Locations
------------------

First, let’s figure out which locations we should use for our analysis.
Let’s grab all ``locations`` from Delhi for all parametrs:

.. code:: ipython3

    api = openaq.OpenAQ()
    
    locations = api.locations(city='Delhi', df=True)
    
    locations.location




.. parsed-literal::

    0                                      Anand Vihar
    1                        Anand Vihar, Delhi - DPCC
    2                           Aya Nagar, Delhi - IMD
    3                     Burari Crossing, Delhi - IMD
    4                   CRRI Mathura Road, Delhi - IMD
    5                                      Civil Lines
    6                     Delhi College Of Engineering
    7                   Delhi Technological University
    8     Delhi Technological University, Delhi - CPCB
    9                                 East Arjun Nagar
    10                     East Arjun Nagar-Delhi CPCB
    11                                     IGI Airport
    12             IGI Airport Terminal-3, Delhi - IMD
    13                                           IHBAS
    14                             IHBAS, Delhi - CPCB
    15                               Income Tax Office
    16                 Income Tax Office, Delhi - CPCB
    17                         Lodhi Road, Delhi - IMD
    18                                     Mandir Marg
    19                       Mandir Marg, Delhi - DPCC
    20                                     NSIT Dwarka
    21                       NSIT Dwarka, Delhi - CPCB
    22                       North Campus, Delhi - IMD
    23                                    Punjabi Bagh
    24                      Punjabi Bagh, Delhi - DPCC
    25                               Pusa, Delhi - IMD
    26                                       Pusa2 IMD
    27                                       R K Puram
    28                         R K Puram, Delhi - DPCC
    29                                        RK Puram
    30                                        Shadipur
    31                          Shadipur, Delhi - CPCB
    32                                       Siri Fort
    33                          Sirifort, Delhi - CPCB
    34                   US Diplomatic Post: New Delhi
    Name: location, dtype: object



Let’s go ahead and filter our results to only grab locations that have
been updated in 2017 and have at least 100 data points.

.. code:: ipython3

    locations = locations.query("count > 100").query("lastUpdated >= '2017-03-01'")
    
    locations.location




.. parsed-literal::

    0                                      Anand Vihar
    1                        Anand Vihar, Delhi - DPCC
    2                           Aya Nagar, Delhi - IMD
    3                     Burari Crossing, Delhi - IMD
    4                   CRRI Mathura Road, Delhi - IMD
    7                   Delhi Technological University
    8     Delhi Technological University, Delhi - CPCB
    10                     East Arjun Nagar-Delhi CPCB
    12             IGI Airport Terminal-3, Delhi - IMD
    13                                           IHBAS
    14                             IHBAS, Delhi - CPCB
    15                               Income Tax Office
    16                 Income Tax Office, Delhi - CPCB
    17                         Lodhi Road, Delhi - IMD
    18                                     Mandir Marg
    19                       Mandir Marg, Delhi - DPCC
    20                                     NSIT Dwarka
    21                       NSIT Dwarka, Delhi - CPCB
    22                       North Campus, Delhi - IMD
    23                                    Punjabi Bagh
    24                      Punjabi Bagh, Delhi - DPCC
    25                               Pusa, Delhi - IMD
    27                                       R K Puram
    28                         R K Puram, Delhi - DPCC
    30                                        Shadipur
    31                          Shadipur, Delhi - CPCB
    32                                       Siri Fort
    33                          Sirifort, Delhi - CPCB
    34                   US Diplomatic Post: New Delhi
    Name: location, dtype: object



Now that we have several up-to-date locations in Delhi we can use, let’s
see what parameters we have to play with!

.. code:: ipython3

    params = []
    
    for i, r in locations.iterrows():
        [params.append(x) for x in r.parameters if x not in params]
        
    params




.. parsed-literal::

    ['pm10', 'so2', 'co', 'no2', 'o3', 'pm25']



Great. Now we have a list of parameters that we can evaluate.
