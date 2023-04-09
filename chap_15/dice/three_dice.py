import plotly.express as px
from die import Die

# Create two D6 dice (6-sides die)
die_1 = Die()
die_2 = Die()
die_3 = Die()

# Make some rolls, and store results in a list
times = 50_000
results = [die_1.roll() + die_2.roll() + die_3.roll() for i in range(times)]

# Analyze the results
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
poss_results = range(3, max_result + 1)
frequencies = [results.count(value) for value in poss_results]

# Visualize the results
# title = f"Results of Rolling a D{die_1.num_sides} and a D{die_2.num_sides} Dice {times} Times"
labels = {'x': 'Result', 'y': 'Frequency of result'}
fig = px.bar(x=poss_results, y=frequencies, labels=labels)

# Further customize chart
fig.update_layout(xaxis_dtick=1)
# fig.show()
file_name = f'html/3 dice.html'
fig.write_html(file_name)
