# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 11:07:57 2022

@author: sorgato
"""


def boxplot_GENERAL(df, year, param1, param2):
    import os, sys
    import pandas as pd
    import plotly.express as px
    import numpy as np
    import plotly.graph_objs as go
    from dash import Dash, dcc, html
    from dash.dependencies import Input, Output

    ye = np.empty(len(df))
    for i in range(0, len(df)):
        ye[i] = df['DATEINTERV'][i].year
    df['year'] = ye
    nan = str('nan')
    list_param0 = np.array(df[param1].unique())
    list_param1 = list_param0[~pd.isnull(list_param0)]
    app = Dash(__name__)

    app.layout = html.Div([
        dcc.Graph(id='graph-with-slider'),
        dcc.Dropdown(
            id='p1',
            options=[{'label': i, 'value': i} for i in list_param1],
            value=list_param1[0],
            multi=False,
            clearable=False,
            style={"width": "50%"}
        ),
        html.P("Values:"),
        dcc.Dropdown(id='values',
                     options=['DOSE Gycm2', 'TEMPS (s)'],
                     value='DOSE Gycm2', clearable=False
                     )
    ])

    @app.callback(
        Output('graph-with-slider', 'figure'),
        Input('p1', 'value'),
        Input('values', 'value')
    )
    def update_figure(p1, values):
        filtered_df = df[df[param1] == p1]
        fig = px.box(filtered_df, x="year", y=values, color=param2, hover_name=param2)

        fig.update_xaxes(tick0=1, dtick=1)
        fig.update_yaxes(type='linear', autorange=True)
        fig.update_layout(transition_duration=100)
        fig.update_layout(clickmode='event+select')
        fig.update_traces(marker_size=5)
        return fig

    if __name__ == 'boxplot_GENERAL':
        # app.run_server(host='localhost', port=8005)
        app.run_server(debug=True)
