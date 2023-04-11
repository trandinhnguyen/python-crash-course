from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime


def extract(file_path):
    path = Path(file_path)
    lines = path.read_text().splitlines()
    reader = csv.reader(lines)
    header_row = next(reader)
    index_high = header_row.index('TMAX')
    index_low = header_row.index('TMIN')

    dates, highs, lows = [], [], []
    for row in reader:
        date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            high = int(row[index_high])
            low = int(row[index_low])
        except ValueError:
            print(f'Missing data for {date}')
        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)

    return dates, highs, lows


dates_sitka, highs_sitka, lows_sitka = extract(
    'weather_data\sitka_weather_2021_simple.csv')
dates_death, highs_death, lows_death = extract(
    'weather_data\death_valley_2021_simple.csv')

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates_sitka, highs_sitka, color='red', alpha=0.6)
ax.plot(dates_sitka, lows_sitka, color='blue', alpha=0.6)
ax.fill_between(dates_sitka, highs_sitka, lows_sitka,
                facecolor='blue', alpha=0.15)

ax.plot(dates_death, highs_death, color='red', alpha=0.3)
ax.plot(dates_death, lows_death, color='blue', alpha=0.3)
ax.fill_between(dates_death, highs_death, lows_death,
                facecolor='blue', alpha=0.05)

# Format plot
ax.set_title(
    "Temperature in Sitka and Death Valley, 2021", fontsize=20)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("", fontsize=16)
ax.set_ylim(0, 140)
ax.tick_params(labelsize=16)

plt.show()
