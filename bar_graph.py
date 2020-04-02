import plotly.express as px
import requests
import pandas as pd
country = input("Enter a country: ")
status = input("Enter case [confirmed, recovered, deaths]: ")

path = 'https://api.covid19api.com/dayone/country/' + country + '/status/' + status + '/live'
all_cases = requests.get(path)
df = pd.read_json(all_cases.text)
titleVar = 'BAR GRAPH: Live COVID-19 ' + status + ' cases '
fig = px.bar(df,
             x='Date',
             y='Cases',
             color='Cases',
             labels={'pop': 'population of Canada'},
             height=600,
             title=titleVar)

#______________Dash Script
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div([dcc.Graph(figure=fig)])

app.run_server(debug=True, port=8066, use_reloader=False)