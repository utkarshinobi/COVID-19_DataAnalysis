import plotly.express as px
import requests
import pandas as pd
import json
pd.set_option('display.max_columns', None)

df1 = px.data.gapminder()
getData = requests.get('https://api.covid19api.com/summary')
dictVals = (eval(getData.text))
listVals = dictVals['Countries']

df2 = pd.read_json(json.dumps(listVals))
dfinal = df1.merge(df2, how='inner', left_on='country', right_on='Country')
titleVar = 'MAP: Live COVID-19 confirmed cases around the world.'
fig = px.scatter_geo(dfinal,
                     locations="iso_alpha",
                     color="continent",
                     hover_name="country",
                     size="TotalConfirmed",
                     projection="natural earth",
                     width=1200,
                     height=700)

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div([dcc.Graph(figure=fig)])

app.run_server(debug=True, port=8052, use_reloader=False)