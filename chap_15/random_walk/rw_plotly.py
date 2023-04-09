import plotly.express as px
from random_walk import RandomWalk

rw = RandomWalk(20_000)
rw.fill_walk()

point_numbers = range(rw.num_points)

fig = px.scatter(x=rw.x_values, y=rw.y_values)

file_name = f'html/rw_plotly.html'
fig.write_html(file_name)