# -*- coding: utf-8 -*-

# stats=stats_med
"""
Created on Mon Mar 21 11:07:57 2022

@author: sorgato
"""
def pie_nb(stats, year):
    from dash import Dash, dcc, html, Input, Output
    import plotly.express as px
    import os
    import pandas as pd
    
    app = Dash(__name__)
    
    
    # dir=r"N:\Themes\Radioprotection GHM\PYTHON_VSO\NRLs\spyder" 
    # os.chdir(dir)
    # df_pie=pd.read_excel ('stats_cat.xlsx', 'Feuil1')
    df_pie=stats
    
    app.layout = html.Div([
        html.Div([
    
            html.Div([
                dcc.Dropdown(
                    df_pie['ampli'].unique(),
                    'VARIC',
                    id='ampli'
                ),
            ], style={'width': '10%', 'display': 'inline-block'}),
    
            # html.Div([
            #     dcc.Dropdown(
            #         df['Indicator Name'].unique(),
            #         'Life expectancy at birth, total (years)',
            #         id='yaxis-column'
            #     ),
            #     dcc.RadioItems(
            #         ['Linear', 'Log'],
            #         'Linear',
            #         id='yaxis-type',
            #         inline=True
            #     )
            # ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
        ]),
    
        dcc.Graph(id='pie'),
    
        # dcc.Slider(
        #     df['Year'].min(),
        #     df['Year'].max(),
        #     step=None,
        #     id='year--slider',
        #     value=df['Year'].max(),
        #     marks={str(year): str(year) for year in df['Year'].unique()},
    
        # )
    ])
    
    
    @app.callback(
        Output('pie', 'figure'),
        Input('ampli', 'value'),
        # Input('yaxis-column', 'value'),
        # Input('xaxis-type', 'value'),
        # Input('yaxis-type', 'value'),
        # Input('year--slider', 'value')
        )
    def update_graph(ampli):
        # dff = df[df['Year'] == year_value]
        fig = px.pie(df_pie[df_pie['ampli']==ampli], values=val, names=column, title='Distribution actes')
                     
                     # x=dff[dff['Indicator Name'] == xaxis_column_name]['Value'],
                     #     y=dff[dff['Indicator Name'] == yaxis_column_name]['Value'],
                     #     hover_name=dff[dff['Indicator Name'] == yaxis_column_name]['Country Name'])
    
        # fig.update_layout(title_x=0.5)
        fig.update_layout(title_text= str(year), margin={'l': 0, 'b': 0, 't': 100, 'r': 0}, hovermode='closest', title_x=0.5, height=500)
        fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20)
        # fig.update_xaxes(title=xaxis_column_name,
        #                  type='linear' if xaxis_type == 'Linear' else 'log')
    
        # fig.update_yaxes(title=yaxis_column_name,
        #                  type='linear' if yaxis_type == 'Linear' else 'log')
    
        return fig
    
    
    if __name__ == '__main__':
        app.run_server(debug=False)
        
