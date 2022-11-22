# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 11:07:57 2022

@author: sorgato
"""

def pie_GENERAL_1paramf(stats):
    from dash import Dash, dcc, html
    import plotly.express as px
    from dash.dependencies import Input, Output

    df_pie = stats
    year=df_pie['Annee'][0][1:-1].split(', ')
    if year[0]==year[-1]:
        year=year[0]
    param1=df_pie.columns[2]
    list_param1=df_pie[param1].unique()
    app = Dash(__name__)
    server = app.server

    app.layout = html.Div([
        html.Div([
            # html.H4(['Distribution '+param1+' - '+param2+', Année:'+year], style={'textAlign': 'center'}),
            dcc.Graph(id="graph"),
            # html.P(param1+" :"),
            # dcc.Dropdown(
            #     id='p1',
            #     options=[{'label': y, 'value': y} for y in list_param1],
            #     value=list_param1[0],
            #     multi=False,
            #     clearable=False,
            #     style={"width": "50%"}
            # ),
            html.P("Values:"),
            dcc.Dropdown(id='values',
                         options=['Nbtotal','PKS_moyen(Gycm2)','Temps_moyen(s)'],
                         value='PKS_moyen(Gycm2)',
                         clearable=False,
                         style={"width": "50%"}
                         ),
        ]),


    ])

    @app.callback(
        Output("graph", "figure"),
        Input("values", "value"))

    def update_graph(p1, values):
        df = df_pie
        fig = px.pie(df,  values=values, hole=.3)
        fig.update_layout(margin={'l': 0, 'b': 10, 't': 50, 'r': 10}, hovermode='closest', title_x=0.5, height=500, uniformtext_minsize=12)
        fig.update_layout(title_text= values +' '+year, title_font_size=30)
        fig.update_traces(hoverinfo='label+percent', textposition='inside', insidetextorientation='radial', textinfo='value+label', textfont_size=10, domain_x=[0, 1])
        return fig


    if __name__ == 'pie_GENERAL_1param':
        app.run_server(host='localhost', port=8005)