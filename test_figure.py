# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 17:12:56 2022

@author: sorgato
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 20:43:17 2022

@author: sorgato
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 13:02:09 2022

@author: sorgato
"""     
        
def fig_int (df, year):
    import plotly.graph_objs as go
    import plotly.io as pio
    import numpy as np
    from datetime import timedelta 
    from datetime import datetime 
    import pandas as pd
    from plotly.subplots import make_subplots
    # pio.renderers.default = 'svg'
    pio.renderers.default = 'browser'
   
    from dash import Dash, html, dcc, Input, Output
    import plotly.express as px
    

    fig5 = go.Figure(px.pie(stats_cat, values='nbtotal', names='categorie', title='Distribution actes'))   
    
    fig5.update_layout(
            updatemenus=[   
                 {
                    # "y": 1 - (i / 5),
                    "buttons": [
                        {
                                "label": ampli,
                                "method": "update",
                                "args":[{"values": stats_cat.loc[stats_cat[menuampli].eq(ampli)].nbtotal, stats_cat.loc[stats_cat[menuampli].eq(ampli)].categorie]}]
                                "args": 
                                    [
                                        {
                                                "values": stats_cat.loc[stats_cat[menuampli].eq(ampli)].nbtotal.T.values,
                                                "names": stats_cat.loc[stats_cat[menuampli].eq(ampli)].categorie.T.values
                                                  # if cat == "All"
                                                 # else  stats_cat.loc[stats_cat[menu].eq(c)].T.values
                                        }
                                    ],
                        }
                        for ampli in stats_cat['ampli'].unique().tolist()
                    ],   
                 }
                for i, menuampli in enumerate(["ampli"])
            ],
        )
    
    fig5.show()   

fig5 = go.Figure(px.pie(stats_cat.loc[stats_cat['ampli'].eq('CIOS')].categorie.T.values, values='nbtotal', names='categorie', title='Distribution actes')) 

    df = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")
    df.loc[df['pop'] < 2.e6, 'country'] = 'Other countries' # Represent only large countries
    fig = px.pie(df, values='pop', names='country', title='Population of European continent')
    fig.show()


fig5 = go.Figure(px.pie(stats_cat, values='nbtotal', names='categorie', title='Distribution actes'))
fig5.update_layout(
    updatemenus=[
        dict(
            type="buttons",
            direction="right",
            x=0.7,
            y=1.2,
            showactive=True,
            buttons=list(
                [
                    dict(
                        label="Cones",
                        method="update",
                        args=[{"y": [df["ice_cream_cones"], df["drinks"]]}],
                    ),
                    dict(
                        label="Scoops",
                        method="update",
                        args=[{"y": [df["scoops"], df["drinks"]]}],
                    ),
                ]
            ),
        )
    ]
)
    # fig3 = go.Figure(go.Table(header={"values": stats_cols}, cells={"values": stats_cat.T.values}))
    fig4.update_layout(
            updatemenus=[   
                {
                    "y": 1 - (i / 5),
                    "buttons": [
                        {
                            "label": ampli,
                            "method": "restyle",
                            "args": [
                                {
                                    "cells": {
                                        "values":  stats_cat.loc[stats_cat[menu].eq(ampli)].T.values
                                          # if cat == "All"
                                         # else  stats_cat.loc[stats_cat[menu].eq(c)].T.values
                                    }
                                }
                            ],
                        }
                        for ampli in stats_cat[menu].unique().tolist()
                    ],   
                }
                for i, menu in enumerate(["ampli"])
            ]
        )
    
    fig3.show()   
    fig4.show() 
    



# JE SUIS RESTEE LA!!!
   #add time info selection
    # https://dash.plotly.com/interactive-graphing
    
 #   external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

 #   app = Dash(__name__, external_stylesheets=external_stylesheets)

 #    # df = pd.read_csv('https://plotly.github.io/datasets/country_indicators.csv')


 #    app.layout = html.Div([
 #        # html.Div([
    
 #        #     html.Div([
 #        #         dcc.Dropdown(
 #        #             df['Indicator Name'].unique(),
 #        #             'Fertility rate, total (births per woman)',
 #        #             id='crossfilter-xaxis-column',
 #        #         ),
 #        #         dcc.RadioItems(
 #        #             ['Linear', 'Log'],
 #        #             'Linear',
 #        #             id='crossfilter-xaxis-type',
 #        #             labelStyle={'display': 'inline-block', 'marginTop': '5px'}
 #        #         )
 #        #     ],
 #        #     style={'width': '49%', 'display': 'inline-block'}),
    
 #        #     html.Div([
 #        #         dcc.Dropdown(
 #        #             df['Indicator Name'].unique(),
 #        #             'Life expectancy at birth, total (years)',
 #        #             id='crossfilter-yaxis-column'
 #        #         ),
 #        #         dcc.RadioItems(
 #        #             ['Linear', 'Log'],
 #        #             'Linear',
 #        #             id='crossfilter-yaxis-type',
 #        #             labelStyle={'display': 'inline-block', 'marginTop': '5px'}
 #        #         )
 #        #     ], style={'width': '49%', 'float': 'right', 'display': 'inline-block'})
 #        # ], style={
 #        #     'padding': '10px 5px'
 #        # }),
    
 #        html.Div([
 #            dcc.Graph(
 #                id='crossfilter-indicator-scatter',
 #                hoverData={'points': [{'customdata': 'Japan'}]}
 #            )
 #        ], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),
 #        html.Div([
 #            dcc.Graph(id='x-time-series'),
 #            dcc.Graph(id='y-time-series'),
 #        ], style={'display': 'inline-block', 'width': '49%'}),
    
 #        html.Div(dcc.Slider(
 #            df['DATEINTERV'].dt.year.min(),
 #            df['DATEINTERV'].dt.year.max(),
 #            step=None,
 #            id='crossfilter-year--slider',
 #            value=df['DATEINTERV'].dt.year.max(),
 #            marks={str(year): str(year) for year in df['DATEINTERV'].dt.year.unique()}
 #        ), style={'width': '49%', 'padding': '0px 20px 20px 20px'})
 #    ])
        
        
 # def update_graph(fig3, name='', xaxis_type='linear', yaxis_type='linear', dff=0):              
 #    fig3.add_trace(
 #                go.Scatter(x=mat['DATEINTERV'][mat['CATEGORY']== name],
 #                           y=mat['DATEINTERV'][mat['CATEGORY']== name],
 #                           hover_name=name, visible = (i==0)  
 #                           ))

 #    # fig3.update_traces(customdata=dff[dff['Indicator Name'] == yaxis_column_name]['Country Name'])

 #    fig3.update_xaxes(title='Date', type='linear' if xaxis_type == 'Linear' else 'log')

 #    fig3.update_yaxes(title='Dose', type='linear' if yaxis_type == 'Linear' else 'log')

 #    fig3.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

 #    return fig3       
        
        
   # -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 20:43:17 2022

@author: sorgato
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 13:02:09 2022

@author: sorgato
"""     
        
def fig_int (df, year):
    import plotly.graph_objs as go
    import plotly.io as pio
    import numpy as np
    from datetime import timedelta 
    from datetime import datetime 
    import pandas as pd
    from plotly.subplots import make_subplots
    # pio.renderers.default = 'svg'
    pio.renderers.default = 'browser'
   
    mat_y=[]
    mat_y=df[df['DATEINTERV'].dt.year==year] 
   
    fig3 = make_subplots(
        rows=1, cols=2,
        specs=[[{"type": "scatter"}, {"type": "table"}]]
    )

    fig4 = make_subplots(
        rows=1, cols=2,
        specs=[[{"type": "scatter"}, {"type": "table"}]]
    )
    
    buttons = []
    buttons2 = []
    # stats = pd.DataFrame([], columns=['annee', 'ampli', 'categorie', 'nbtotal', 'moyenne', 'ecart-type'])
    stats = pd.DataFrame([], columns=['annee', 'ampli', 'categorie', 'nbtotal', 'moyenne', 'ecartType'])
    stats_list=[]
    args2=[]
    i = 0
    ampli_list = list(mat_y['AMPLI'].unique())  

    t_curves=0
    for ampli in ampli_list:
        mat=mat_y[mat_y['AMPLI']==ampli] 
        cat_list = list(mat['CATEGORY'].unique()) 
        t_curves+=len(cat_list)
    args = [False] * t_curves
       
    
    l_curve=0
    for ampli in ampli_list:
        
        mat=[]
        mat=mat_y[mat_y['AMPLI']==ampli]           


        cat_list = []
        cat_list = list(mat['CATEGORY'].unique()) 
        c=0
        # args2=[]
        for cat in cat_list:  
            yy=[]

            matint=[]
            matint=mat['DATEINTERV'][mat['CATEGORY']==cat]
            t=matint.dt.date.value_counts()
            tch=pd.to_datetime(t.index[t>1])
            for tst in matint:
                if tst in tch:
                    st=matint[matint==tst]
                    for j in range(0, len(st)):                        
                        st.iloc[j]=pd.to_datetime(st.iloc[j] + pd.DateOffset(hour=j))                        
                    
                    mat['DATEINTERV'].loc[st.index]=pd.to_datetime(st)   
                    
            yy=mat['DOSE Gycm2'][mat['CATEGORY']==cat]
            
            stats_list.append([year, ampli, cat, len(yy), round(yy.mean(),3), round(yy.std(),3)])
            
            fig3.add_trace(
                go.Scatter(
                    x = mat['DATEINTERV'][mat['CATEGORY']==cat],
                    y = yy,
                    # y = mat['TEMPS (s)'][mat['CATEGORY']==cat],
                    name = cat, visible = (i==0)), 
                    row=1, col=1)
            
            stats= pd.DataFrame(stats_list)
            stats.columns=['annee', 'ampli', 'categorie', 'nbtotal', 'moyenne', 'ecartType']
        
        # stats_cols=stats_cat.columns[-5:]
        # stats_cat=pd.DataFrame(stats[stats_cols])
        # stats_cols=stats_cat.index[-5:]

# je suis làààààà      https://stackoverflow.com/questions/69568250/interactive-filtering-data-table-in-plotly-by-using-a-dropdown 
    

                    # fig3.add_trace(go.Table(
                    # columnwidth = [80,50],
                    # header=dict(values=list(stats_cols),
                    #             fill_color='paleturquoise',
                    #             align='left'),
                    # cells=dict(values=[stats_cat.iloc[xx] for xx, cols in enumerate(stats_cols)],
                    #             fill_color='white',
                    #             align='left'),
                    #             visible = True), row=1, col=2)
                
            # args2.append([ {"cells": {"values": stats_cat.T.values } } ])                        
            # args2= [
            #     {
            #         "cells": {
            #             "values": stats.T.values
            #         }
            #     }
            # ]

            # c+=1           
            # l_curve+=1    


       # {"values": [scores[x] for x in scores_cols]   
        # stats= pd.DataFrame(stats_list)
        # stats.columns=['annee', 'ampli', 'categorie', 'nbtotal', 'moyenne', 'ecartType']

        args = [False] * t_curves        
        args[l_curve:len(cat_list)+l_curve] = [True] * len(cat_list)
        #i is an iterable used to tell our "args" list which value to set to True
        i+=1
        l_curve+=len(cat_list)

        button1 = dict(label = ampli,
                      method = "update",
                      args=[{"visible": args}])
        buttons.append(button1)

        
    fig3.update_layout(updatemenus=[dict(active=0,
                          type="dropdown",
                          buttons=buttons,
                          x = 0,
                          y = 1.1,
                          xanchor = 'left',
                          yanchor = 'bottom'
                          ),
                    ])

        # button1 = dict(label = ampli,
        #               method = "update",
        #               args=[{"visible": args}])
        # buttons1.append(button1)

        # button2 = dict(label = ampli,
        #               method = "restyle",
        #               args=[{"visible": args}])
        # buttons2.append(button2)

        
        # args2 = [False] * t_curves         
        # args2[l_curve:len(cat_list)+l_curve] = [True] * len(cat_list)


        # i+=1
        

        
    # fig3.update_layout(updatemenus=[dict(active=0,
    #                       type="dropdown",
    #                       buttons=buttons2,
    #                       x = 0,
    #                       y = 1.1,
    #                       xanchor = 'left',
    #                       yanchor = 'bottom'
    #                       )])


    # fig3.update_layout(
    # updatemenus=[
    #     dict(
    #         buttons=buttons2,
    #         direction="down",
    #         pad={"r": 10, "t": 10},
    #         showactive=True,
    #         x = 0.01,
    #         y = 1.3,
    #         xanchor="left",
    #         yanchor="top")
    #         ])
    
    # updatemenus=[dict(active=0,
    #                       type="dropdown",
    #                       buttons=buttons2,
    #                       x = 0,
    #                       y = 1.1,
    #                       xanchor = 'left',
    #                       yanchor = 'bottom'
    #                       )]
    
    # fig3.update_layout = dict(title = 'test', showlegend=False, updatemenus=updatemenus)

    # # fig3.update_layout(updatemenus=[dict(active=0,
    #                       type="dropdown",
    #                       buttons=buttons1,
    #                       x = 0,
    #                       y = 1.1,
    #                       xanchor = 'left',
    #                       yanchor = 'bottom'
    #                       )],
    #                     selector=dict(type="table"))
   

    fig3.update_yaxes(title_text="DOSE (Gycm^{2})", row=1, col=1)

    fig3.update_layout(
    autosize=True,
    # width=1000,
    # height=800,
    title_text="NRL année " + str(year),
    title_x=0.5)
    
   
    stats_cols=stats.columns[-5:]
    stats_cat=pd.DataFrame(stats[stats_cols])
    fig4= go.Figure(go.Table(
                    columnwidth = [80,50],
                    header=dict(values=list(stats_cols),
                                fill_color='paleturquoise',
                                align='left'),
                    cells={"values": stats_cat.T.values},
                                # fill_color='white',
                                 # align='left'
                                # visible = True
                                ))

                 
    # fig3 = go.Figure(go.Table(header={"values": stats_cols}, cells={"values": stats_cat.T.values}))
    fig4.update_layout(
            updatemenus=[   
                {
                    "y": 1 - (i / 5),
                    "buttons": [
                        {
                            "label": ampli,
                            "method": "restyle",
                            "args": [
                                {
                                    "cells": {
                                        "values":  stats_cat.loc[stats_cat[menu].eq(ampli)].T.values
                                          # if cat == "All"
                                         # else  stats_cat.loc[stats_cat[menu].eq(c)].T.values
                                    }
                                }
                            ],
                        }
                        for ampli in stats_cat[menu].unique().tolist()
                    ],   
                }
                for i, menu in enumerate(["ampli"])
            ]
        )
    
    fig3.show()   
    fig4.show() 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
  # example that works  
#     import plotly.graph_objects as go

df = pd.DataFrame(
    {
        "Date": ["2020-01-27", "2020-02-27", "2020-03-27"],
        "A_item": [2, 8, 0],
        "B_item": [1, 7, 10],
        "C_item": [9, 2, 9],
        "Channel_type": ["Channel_1", "Channel_1", "Channel_2"],
    }
)

fig = go.Figure(go.Table(header={"values": df.columns}, cells={"values": df.T.values}))
fig.update_layout(
    updatemenus=[
        {
            "y": 1 - (i / 5),
            "buttons": [
                {
                    "label": c,
                    "method": "restyle",
                    "args": [
                        {
                            "cells": {
                                "values": df.loc[df[menu].eq(c)].T.values
                                # if c == "All"
                                # else df.loc[df[menu].eq(c)].T.values
                            }
                        }
                    ],
                }
                for c in df[menu].unique().tolist()
            ],
        }
        for i, menu in enumerate(["Channel_type"])
    ]
)


# fig = make_subplots(
#     rows=3, cols=1,
#     shared_xaxes=True,
#     vertical_spacing=0.03,
#     specs=[[{"type": "table"}],
#            [{"type": "scatter"}],
#            [{"type": "scatter"}]]
# )


# another example that works!!
# import plotly.graph_objects as go

# df = pd.DataFrame(
#     {
#         "Date": ["2020-01-27", "2020-02-27", "2020-03-27"],
#         "A_item": [2, 8, 0],
#         "B_item": [1, 7, 10],
#         "C_item": [9, 2, 9],
#         "Channel_type": ["Channel_1", "Channel_1", "Channel_2"],
#     }
# )

# fig = go.Figure(go.Table(header={"values": df.columns}, cells={"values": df.T.values}))
# fig.update_layout(
#     updatemenus=[
#         {
#             "y": 1 - (i / 5),
#             "buttons": [
#                 {
#                     "label": c,
#                     "method": "restyle",
#                     "args": [
#                         {
#                             "cells": {
#                                 "values": df.T.values
#                                 if c == "All"
#                                 else df.loc[df[menu].eq(c)].T.values
#                             }
#                         }
#                     ],
#                 }
#                 for c in ["All"] + df[menu].unique().tolist()
#             ],
#         }
#         for i, menu in enumerate(["Channel_type", "Date"])
#     ]
# )


# fig = make_subplots(
#     rows=3, cols=1,
#     shared_xaxes=True,
#     vertical_spacing=0.03,
#     specs=[[{"type": "table"}],
#             [{"type": "scatter"}],
#             [{"type": "scatter"}]]
# )
