import matplotlib.pyplot as plt
from die import Die

# Create two D6 dice (6-sides die)
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list
results = [die_1.roll() + die_2.roll() for i in range(50_000)]

# Analyze the results
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result + 1)
frequencies = [results.count(value) for value in poss_results]

plt.bar(poss_results, frequencies)

plt.show()
