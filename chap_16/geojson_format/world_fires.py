from pathlib import Path
import csv
import plotly.express as px

path = Path("eq_data/world_fires_1_day.csv")
lines = path.read_text().splitlines()
reader = csv.reader(lines)

header_row = next(reader)

lats, lons, brightness,  = [], [], []
for row in reader:
    lats.append(float(row[0]))
    lons.append(float(row[1]))
    brightness.append(float(row[2]))

title = 'World fires in past 1 day'
fig = px.scatter_geo(lat=lats,
                     lon=lons,
                    #  size=brightness,
                     title=title,
                     color=brightness,
                     color_continuous_scale='YlOrRd',
                     labels={'color': 'Brightness'},
                     projection='natural earth',
                     )
fig.write_html("world_fires.html")
