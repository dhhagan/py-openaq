from .decorators import skipif

try:
    import pandas as pd

    _no_pandas = False
except ImportError:
    _no_pandas = True

try:
    import seaborn as sns
    import matplotlib.pyplot as plt
    import matplotlib.dates as dates

    _no_sns = False
except ImportError:
    _no_sns = True

def tsindex(ax):
    """
        Reset the axis parameters to look nice!
    """
    # Get dt in days
    dt = ax.get_xlim()[-1] - ax.get_xlim()[0]

    if dt <= 1./24.:   # less than one hour
        pass
    elif dt <= 1.:     # less than one day
        ax.xaxis.set_minor_locator( dates.HourLocator() )
        ax.xaxis.set_minor_formatter( dates.DateFormatter(""))

        ax.xaxis.set_major_locator( dates.HourLocator( interval = 3))
        ax.xaxis.set_major_formatter( dates.DateFormatter("%-I %p"))
    elif dt <= 7.:      # less than one week
        ax.xaxis.set_minor_locator( dates.DayLocator())
        ax.xaxis.set_minor_formatter( dates.DateFormatter("%d"))

        ax.xaxis.set_major_locator( dates.DayLocator( bymonthday = [1, 8, 15, 22]) )
        ax.xaxis.set_major_formatter( dates.DateFormatter("\n%b\n%Y") )
    elif dt <= 14.:     # less than two weeks
        ax.xaxis.set_minor_locator( dates.DayLocator())
        ax.xaxis.set_minor_formatter( dates.DateFormatter("%d"))

        ax.xaxis.set_major_locator( dates.DayLocator( bymonthday = [1, 15]) )
        ax.xaxis.set_major_formatter( dates.DateFormatter("\n%b\n%Y") )
    elif dt <= 28.:     # less than four weeks
        ax.xaxis.set_minor_locator( dates.DayLocator())
        ax.xaxis.set_minor_formatter( dates.DateFormatter("%d"))

        ax.xaxis.set_major_locator( dates.MonthLocator() )
        ax.xaxis.set_major_formatter( dates.DateFormatter("\n%b\n%Y") )
    elif dt <= 4 * 30.: # less than four months
        ax.xaxis.set_minor_locator( dates.DayLocator( bymonthday = [1, 7, 14, 21] ))
        ax.xaxis.set_minor_formatter( dates.DateFormatter("%d"))

        ax.xaxis.set_major_locator( dates.MonthLocator())
        ax.xaxis.set_major_formatter( dates.DateFormatter("\n%b\n%Y") )
    else:
        ax.xaxis.set_minor_locator( dates.MonthLocator(interval = 2) )
        ax.xaxis.set_minor_formatter( dates.DateFormatter("%b"))

        ax.xaxis.set_major_locator( dates.MonthLocator(bymonth = [1]) )
        ax.xaxis.set_major_formatter( dates.DateFormatter("\n%Y"))


    return ax

rc_tsplot = {
    'xtick.major.size': 8.,
    'xtick.minor.size': 4.,
    'xtick.direction': 'out',
    'ytick.major.size': 10.,
}

@skipif(_no_sns)
def tsplot(data, time = None, ax = None, parameter = None, rs = '1h',
           locations = None, plot_kws = {}, fmt_axis = True, **kwargs):
    """
    If there are multiple locations && multiple params, issue a warning!

    :param data: dataframe with data
    :param time: column name with time. Defaults to index.
    :param ax: Plot on ax if you would like.
    :param parameter: string with parameter to plot. Can only plot 1 at a time.

    """
    assert isinstance(data, pd.DataFrame), "`data` must be a pandas dataframe"
    assert parameter in [None, 'pm25', 'pm10', 'o3', 'no2', 'bc', 'co', 'so2'], "Invalid parameter"

    if "figsize" not in plot_kws.keys():
        plot_kws['figsize'] = (14, 7)

    if type(locations) is not list:
        locations = [locations]

    if ax is None:
        ax = plt.gca()

    # Deal with ts index issues
    if data.index.name is not time:
        try:
            data.index = data[time]
        except:
            if not isinstance(data.index, pd.tseries.index.DatetimeIndex):
                data.index = data['date.local']

    data.index.name = 'index'

    # If parameter is not defined, use the parameter of the first row
    if parameter is None:
        parameter = data.parameter[0]

    data = data[data['parameter'] == parameter]

    # Iterate over locations!
    for name, group in data.groupby('location'):
        if name in locations or locations[0] is None:
            _y = group.resample(rs).mean()

            ax.plot(_y.value, label = name)

    ax.set_ylabel(parameter)
    ax.legend( loc = 'best' )

    # Set the axes limits
    ax.set_ylim([0, ax.get_ylim()[-1]])

    if fmt_axis:
        ax = tsindex(ax)

    return ax
