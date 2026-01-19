import numpy as np
from bokeh.io import output_notebook, show
from bokeh.plotting import figure

output_notebook()  
fig = figure(width=500, height=300, title='Different Types of Plots')
x = np.linspace(0, 10, 100)
y = np.sin(x)
fig.line(x, y, line_width=2, legend_label='Line Plot')
fig.vbar(x=x, top=y, legend_label='Bar Chart', width=0.5, bottom=0)
fig.scatter(x, y, size=10, color='red', legend_label='Scatter Plot') 
fig.xaxis.axis_label = 'X Axis'
fig.yaxis.axis_label = 'Y Axis'
fig.legend.location = 'top_left'
show(fig)
