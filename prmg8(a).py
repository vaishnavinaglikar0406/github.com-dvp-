from bokeh.plotting import figure, show
from bokeh.models import Legend, LegendItem, Span
from bokeh.io import output_notebook
output_notebook()
x = [1, 2, 3, 4, 5]
y1 = [2, 5, 7, 2, 8]
y2 = [1, 4, 5, 3, 6]
p = figure(title="Line Graph with Annotations and Legends",
           x_axis_label='X-axis', y_axis_label='Y-axis',
           width=600, height=400)
line1 = p.line(x, y1, line_width=2, color="blue")
line2 = p.line(x, y2, line_width=2, color="red")
vline = Span(location=3, dimension='height', line_color='black', line_width=2)
p.add_layout(vline)
legend = Legend(items=[
    LegendItem(label="Line 1", renderers=[line1]),
    LegendItem(label="Line 2", renderers=[line2])
])
p.add_layout(legend, 'right')  # Place legend on the right
show(p)
