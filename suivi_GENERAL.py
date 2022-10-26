# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 11:07:57 2022

@author: sorgato
"""


def suivi_GENERAL(year, param1, param2):
    import os, sys
    import pandas as pd
    import plotly.express as px
    import numpy as np
    import plotly.graph_objs as go
    from dash import Dash, dcc, html
    from dash.dependencies import Input, Output

    dir = sys.path[0] + "\\results\\" + param1 + "-" + param2
    os.chdir(dir)
    stats = []
    for y in range(year[0], year[1] + 1, 1):
        stats = pd.read_excel(str(y) + '_stats.xlsx', 'Feuil1').append(stats)
    stats.reset_index(inplace=True)
    ye = np.empty(len(stats))
    for i in range(0, len(stats)):
        a = stats['Annee'][i]
        a = a.replace('[', '').replace(']', '').split(',')
        ye[i] = int(a[0])
    stats['year'] = ye

    df = stats
    list_param1 = df[param1].unique()
    app = Dash(__name__)

    app.layout = html.Div([
        dcc.Graph(id='graph-with-slider'),
        # html.H2('Sliders'),
        # html.H4('Range1'),
        # dcc.RangeSlider(
        #     df['year'].min(),
        #     df['year'].max(),
        #     step=1,
        #     value=list(map(int, str(int(float(df['year'].min()))))),
        #     marks={str(y) for y in df['year'].unique()},
        #     id='slider1'
        # ),
        # html.H4('Range2'),
        # dcc.RangeSlider(
        #     df['year'].min(),
        #     df['year'].max(),
        #     step=1,
        #     value=list(map(int, str(int(float(df['year'].min()))))),
        #     marks={str(y) for y in df['year'].unique()},
        #     id='slider2'
        # ),
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
                         options=['Nbtotal','PKS_moyen(Gycm2)','Temps_moyen(s)'],
                         value='Nbtotal', clearable=False
                         )
    ])



    @app.callback(
        Output('graph-with-slider', 'figure'),
        Input('p1', 'value'),
        Input('values', 'value')
        # [Input('slider1', 'value'),
        #  Input('slider2', 'value')  # ,
        #  ]
        )
    def update_figure(p1, values):
        # df0=df[year].between(slider1, slider2, inclusive=False)
        filtered_df = df[df[param1] == p1]
        if values=='PKS_moyen(Gycm2)':
            fig = px.scatter(filtered_df, x="year", y=values, color=param2, hover_name=param2, error_y="EcartType(Gycm2)")
        elif values=='Temps_moyen(s)':
            fig = px.scatter(filtered_df, x="year", y=values, color=param2, hover_name=param2, error_y="EcartType(s)")
        else:
            fig = px.scatter(filtered_df, x="year", y=values, color=param2, hover_name=param2)

        fig.update_xaxes(tick0=1, dtick=1)
        fig.update_yaxes(type='linear', autorange= True)
        fig.update_layout(transition_duration=100)
        fig.update_layout(clickmode='event+select')
        fig.update_traces(marker_size=10)
        return fig

    if __name__ == 'suivi_GENERAL':
        # app.run_server(host='localhost', port=8005)
        app.run_server(debug=True)
