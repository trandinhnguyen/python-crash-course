from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

def extract(file_path):
    path = Path(file_path)
    lines = path.read_text().splitlines()
    reader = csv.reader(lines)
    header_row = next(reader)
    index = header_row.index('PRCP')

    dates, rains = [], []
    for row in reader:
        date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            rain = float(row[index])
        except ValueError:
            print(f'Missing data for {date}')
        else:
            dates.append(date)
            rains.append(rain)

    return dates, rains

dates_sitka, rains_sitka = extract('weather_data\sitka_weather_2021_full.csv')
dates_death, rains_death = extract('weather_data\death_valley_2021_full.csv')

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates_sitka, rains_sitka, color='blue', alpha=0.4)
ax.plot(dates_death, rains_death, color='red', alpha=0.8)

# Format plot
ax.set_title(
    "Rainfall in Sitka and Death Valley, 2021", fontsize=20)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
