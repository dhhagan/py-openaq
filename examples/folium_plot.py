import openaq
import folium

api = openaq.OpenAQ()
COUNTRY_COLORS = {'CH': 'red', 'AT': 'cyan'}

locs = {country: api.locations(country=country, df=True)
                 for country in COUNTRY_COLORS.keys()}

basemap = folium.Map(location=[47.4308, 11.8728], zoom_start=6)

for country, color in COUNTRY_COLORS.items():
    print(country,color)
    locs[country].apply(lambda row:  folium.Marker((row['coordinates.latitude'], 
               row['coordinates.longitude']), icon=folium.Icon(color=color),
               popup = row.to_frame().to_html()).add_to(basemap),
               axis=1)

basemap.save('airquality.html')
