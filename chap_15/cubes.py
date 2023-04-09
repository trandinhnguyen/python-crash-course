import matplotlib.pyplot as plt
plt.style.use('seaborn')

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

fix, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greens)

# Set chart title and label axes.
ax.set_title("Cubic numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(labelsize=14)

# Set the range for each axis
# ax.axis([0, 100, 0, 1_100_000])

#  Override the default tick label style for any plot
# ax.ticklabel_format(style='plain')

# plt.savefig('squares_plot.png',
#             bbox_inches='tight'
#             )
plt.show()
