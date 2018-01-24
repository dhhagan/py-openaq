"""
Hawai'i SO2 Timeseries
======================
_thumb: .4, .4
"""
import seaborn as sns
import openaq

sns.set(style="ticks")

api = openaq.OpenAQ()

# grab the data
res = api.measurements(city='Hilo', parameter='so2', limit=10000, df=True)

fig, ax = plt.subplots(1)

for group, df in res.groupby('location'):
    _df = df.query("value >= 0.0").resample('1h').mean()

    ax.plot(_df.value * 1000., label=group)

ax.legend(loc='best')
ax.set_ylabel("$SO_2 \; [ppb]$", fontsize=18)

sns.despine(offset=5)
