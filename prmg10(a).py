import plotly.graph_objects as go 
import plotly.offline as pyo 
import pandas as pd 
tesla = pd.read_csv("D:\dvwithpython_lab\Time-Series-Tesla-StockPrice.csv") 
trace_one = go.Scatter( 
  x=tesla.date, 
  y=tesla['high'], 
  name="Tesla High", 
  line=dict(color='#17BECF'), 
  opacity = 0.8) 
trace_two = go.Scatter( 
  x=tesla.date, 
  y=tesla['low'], 
  name="Tesla Low", 
  line=dict(color='#7F7F7F'), 
  opacity = 0.8) 
data = [trace_one, trace_two] 
layout = dict ( 
  title = 'Tesla Stock Price - High vs Low') 
fig = dict(data=data, layout=layout) 
pyo.plot(fig, filename = 'Tesla Stock Comparison.html') 
