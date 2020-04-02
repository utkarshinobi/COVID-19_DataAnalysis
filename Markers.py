import plotly.express as px
import requests
import pandas as pd
import json
pd.set_option('display.max_columns', None)

getData = requests.get('https://api.covid19api.com/summary')
dictVals = (eval(getData.text))
listVals = dictVals['Countries']
df = pd.read_json(json.dumps(listVals))
titleVar = 'LINE GRAPH: Live COVID-19 Confirmed Cases Markers.'
df2 = df.head(20)
fig = px.line(df,
              x='TotalConfirmed',
              y='NewConfirmed',
              color="Country",
              title=titleVar)
fig.update_traces(mode="markers+lines")
#______________Dash Script
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div([dcc.Graph(figure=fig)])

app.run_server(debug=True, port=8066, use_reloader=False)