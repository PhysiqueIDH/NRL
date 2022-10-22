from dash import Dash, dcc, html
    # import dash_core_components as dcc
    # import dash_html_components as html
    import pandas as pd
    import plotly.express as px
    from dash.dependencies import Input, Output
    data = {'labels': ["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
            'parents': ["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve"],
            'values': [10, 14, 12, 10, 2, 6, 6, 4, 4]}

    # Creates pandas DataFrame.
    df_pie = pd.DataFrame(data)
    df = px.data.tips()
    fig = px.pie(df, values='tip', names='day')
    fig.show()


    # df_pie=stats
    param1=df_pie.columns[0]
    param2=df_pie.columns[1]

    list_param=df_pie[param1].unique().value_counts().index

    app = Dash(__name__)

    app.layout = html.Div([
        html.Div([
            html.Label(['Distribution actes']),
            dcc.Dropdown(
                  id='my_dropdown',
                  options=[{'label': y, 'value': y} for y in list_param],
                  value=list_param[0],
                  multi=False,
                  clearable=False,
                  style={"width": "50%"}
            )
        ]),

        html.Div([
            dcc.Graph(id='the_graph')
        ]),

    ])

    @app.callback(
        Output(component_id='the_graph', component_property='figure'),
        [Input(component_id='my_dropdown', component_property='value')]
    )
    def update_graph(P1):
        piechart = px.pie(
            df_pie[df_pie[param1] == P1],
            values=what,
            names=param2,
            hole=.3,
        )
        return piechart

    if __name__ == '__main__':
        app.run_server(host='localhost', port=8005)


    %%%%%%%%%%%%%%%%%%%%%

    from dash import Dash, dcc, html, Input, Output
    import plotly.express as px

    app = Dash(__name__)

    app.layout = html.Div([
        html.H4('Analysis of the restaurant sales'),
        dcc.Graph(id="graph"),
        html.P("Names:"),
        dcc.Dropdown(id='names',
                     options=['smoker', 'day', 'time', 'sex'],
                     value='day', clearable=False
                     ),
        html.P("Values:"),
        dcc.Dropdown(id='values',
                     options=['total_bill', 'tip', 'size'],
                     value='total_bill', clearable=False
                     ),
    ])


    @app.callback(
        Output("graph", "figure"),
        Input("names", "value"),
        Input("values", "value"))
    def generate_chart(names, values):
        df = px.data.tips()  # replace with your own data source
        fig = px.pie(df, values=values, names=names, hole=.3)
        return fig


    # if __name__ == '__main__':
    app.run_server(host='localhost', port=8006)