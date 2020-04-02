import plotly.express as px
import requests
import pandas as pd
pd.set_option('display.max_columns', None)

country = input("Enter a country: ")
path = 'https://api.covid19api.com/dayone/country/' + country + '/status/confirmed/live'
all_cases = requests.get(path)
df = pd.read_json(all_cases.text)

list_of_cases = df['Cases'].to_list()

new_cases = [0] * len(list_of_cases)

for i in range(0, len(list_of_cases)):
    if ((i + 1) >= 7):
        new_cases[i] = list_of_cases[i] - list_of_cases[i - 6]
        if (new_cases[i] < 0):
            new_cases[i] = 0
    else:
        new_cases[i] = list_of_cases[i]

df['NewCases'] = new_cases
titleVar = 'LINE GRAPH: Live COVID-19 Cases vs. New Cases in ' + country
fig = px.line(df, x='Cases', y='NewCases', title='')
fig.update_layout(xaxis_type="log", yaxis_type="log")

#______________Dash Script
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div([dcc.Graph(figure=fig)])

app.run_server(debug=True, port=8066, use_reloader=False)