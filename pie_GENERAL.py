# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 11:07:57 2022

@author: sorgato
"""
def pie_GENERAL(stats):
    from dash import Dash, dcc, html
    import pandas as pd
    import plotly.express as px
    from dash.dependencies import Input, Output

    df_pie = stats
    year=df_pie['Annee'][0]
    param1=df_pie.columns[2]
    param2=df_pie.columns[3]
    list_param1=df_pie[param1].unique()
    app = Dash(__name__)

    app.layout = html.Div([
        html.Div([
            html.H4(['Distribution '+param1+' - '+param2+', Année:'+year]),
            dcc.Graph(id="graph"),
            html.P(param1+" :"),
            dcc.Dropdown(
                id='p1',
                options=[{'label': y, 'value': y} for y in list_param1],
                value=list_param1[0],
                multi=False,
                clearable=False,
                style={"width": "50%"}
            ),
            dcc.Dropdown(
                  id='p2',
                  options=param2,
                  value=param2,
                  multi=False,
                  clearable=False,
                  style={"width": "50%"}
            ),
            html.P("Values:"),
            dcc.Dropdown(id='values',
                         options=['Nbtotal','Moyenne Gycm2'],
                         value='Nbtotal', clearable=False
                         ),
        ]),


    ])



    @app.callback(
        Output("graph", "figure"),
        Input("p1", "value"),
        Input("p2", "value"),
        Input("values", "value"))

    def update_graph(p1, p2, values):
        df = df_pie[df_pie[param1] == p1]
        fig = px.pie(df,  values=values, names=p2, hole=.3)
        return fig


    if __name__ == '__main__':
        app.run_server(host='localhost', port=8005)

