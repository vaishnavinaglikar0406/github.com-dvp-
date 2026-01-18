import pandas as pd 
import plotly.express as px 
#import data 
data = pd.read_csv('D:\\dvwithpython_lab\\2011_us_ag_exports.csv') 
fig = px.choropleth(data, locations='code', locationmode="USA-states", color='total exports', scope="usa") 
fig.show()
