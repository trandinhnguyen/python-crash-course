from pathlib import Path
import json

# Read data as a string and convert to a Python object
path = Path("eq_data/eq_data_1_day_m1.geojson")
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

# Examine all earthquakes in the dataset
all_eq_dict = all_eq_data['features']

# Extract magnitudes and locations
mags, lons, lats = [], [], []
for eq_dict in all_eq_dict:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]

    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(lons[:10])
print(lats[:10])