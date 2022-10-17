# -*- coding: utf-8 -*-

# stats=stats_med
"""
Created on Mon Mar 21 11:07:57 2022

@author: sorgato
"""
def pie_GENERAL(stats, what):
    from dash import Dash, dcc, html
    # import dash_core_components as dcc
    # import dash_html_components as html
    import pandas as pd
    import plotly.express as px
    from dash.dependencies import Input, Output

    df_pie=stats

    param1=df_pie.columns[2]
    param2=df_pie.columns[3]

    list_param=df_pie[param1].unique()

    app = Dash(__name__)

    app.layout = html.Div([
        html.Div([
            html.H4(['Distribution '+param1+' - '+param2]),
            dcc.Graph(id="graph"),
            html.P(param1+" :"),
            dcc.Dropdown(
                  id='names',
                  options=[{'label': y, 'value': y} for y in list_param],
                  value=list_param[0],
                  multi=False,
                  clearable=False,
                  style={"width": "50%"}
            ),
            html.P("Values:"),
            dcc.Dropdown(id='values',
                         options=what,
                         value='Nbtotal', clearable=False
                         ),
        ]),


    ])

    @app.callback(
        Output("graph", "figure"),
        Input("names", "value"),
        Input("values", "value"))
    def generate_chart(names, values):
        df = stats  # replace with your own data source
        fig = px.pie(df,  values=values, names=names, hole=.3)
        return fig

    if __name__ == '__main__':
        app.run_server(host='localhost', port=8005)

