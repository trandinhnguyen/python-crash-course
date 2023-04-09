import plotly.express as px
from die import Die

die_1 = Die(8)
die_2 = Die(8)

# Make some rolls, and store results in a list
times = 50_000
results = [die_1.roll() + die_2.roll() for i in range(times)]

# Analyze the results
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result + 1)
frequencies = [results.count(value) for value in poss_results]

# Visualize the results
title = f"Results of Rolling a D{die_1.num_sides} and a D{die_2.num_sides} Dice {times} Times"
labels = {'x': 'Result', 'y': 'Frequency of result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customize chart
fig.update_layout(xaxis_dtick=1)
# fig.show()
file_name = f'html/D{die_1.num_sides}_and_D{die_2.num_sides} dice.html'
fig.write_html(file_name)
