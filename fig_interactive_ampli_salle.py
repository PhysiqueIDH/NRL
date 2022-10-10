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
        
def fig_int_ampli_salle (df, year):
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
   
    fig3 = go.Figure()
    fig4 = go.Figure()
    stats_ampli_salle = pd.DataFrame([], columns=['annee',  'salle', 'ampli', 'nbtotal', 'moyenne Gycm2', 'ecartType', 'median Gycm2'])
    stats_ampli_salle_list=[]
    
    
    buttons1 = []
    i = 0 
    salle_list = []
    salle_list = list(mat_y['SALLE'].unique()) 
        
    t_curves=0
    for salle in salle_list:
        mat=mat_y[mat_y['SALLE']==salle] 
        ampli_list = list(mat['AMPLI'].unique()) 
        t_curves+=len(ampli_list)
    args = [False] * t_curves
       
    
    l_curve=0
    for salle in salle_list:

        mat=[]
        mat=mat_y[mat_y['SALLE']==salle]                    

        ampli_list = []
        ampli_list = list(mat['AMPLI'].unique()) 
        for ampli in ampli_list:      
            matint=[]
            # yy=mat['DATEINTERV'][mat['SALLE']==salle]
            # t=matint.dt.date.value_counts()
            # tch=pd.to_datetime(t.index[t>1])
            # for tst in matint:
            #     if tst in tch:
            #         st=matint[matint==tst]
            #         for j in range(0, len(st)):                        
            #             st.iloc[j]=pd.to_datetime(st.iloc[j] + pd.DateOffset(hour=j))                        
                    
            #         mat['DATEINTERV'].loc[st.index]=pd.to_datetime(st)                
            
            yy=mat['DOSE Gycm2'][mat['AMPLI']==ampli]
            
            stats_ampli_salle_list.append([year, salle, ampli, len(yy), round(yy.mean(),3), round(yy.std(),3), round(yy.median(),3)])
            
            fig3.add_trace(
                go.Scatter(
                    x = mat['DATEINTERV'][mat['AMPLI']==ampli],
                    y = yy,
                    # y = mat['TEMPS (s)'][mat['CATEGORY']==cat],
                    name = ampli, visible = (i==0)))
                    
            
            stats= pd.DataFrame(stats_ampli_salle_list)
            stats.columns=['annee',  'salle', 'ampli', 'nbtotal', 'moyenne Gycm2', 'ecartType', 'median Gycm2']  


        args = [False] * t_curves        
        args[l_curve:i*len(ampli_list)+len(ampli_list)] = [True] * len(ampli_list)
        # args[l_curve:len(cat_list)+l_curve] = [True] * len(cat_list) #also works
        #i is an iterable used to tell our "args" list which value to set to True
        i+=1
        l_curve+=len(ampli_list)

        button1 = dict(label = salle,
                      method = "update",
                      args=[{"visible": args}])
        buttons1.append(button1)

        
    fig3.update_layout(updatemenus=[dict(active=0,
                          type="dropdown",
                          buttons=buttons1,
                          x = 0,
                          y = 1.1,
                          xanchor = 'left',
                          yanchor = 'bottom'
                          ),
                    ])
   

    fig3.update_yaxes(
            title_text = "PDS (Gycm2=100µGym2)",
            # title_text = "temps (s)",
            title_standoff = 25)
    
      
    fig3.update_layout(
    autosize=True,
    # width=1000,
    # height=800,
    title_text="Utilisation salles " + str(year),
    title_x=0.5)
            
    fig3.update_layout(
    autosize=False,
    width=1000,
    height=800)

    fig3.show()     
    
    ytot=mat_y['DOSE Gycm2']
    stats_ampli_salle_list.append([year, 'TOTAL', ampli,  len(ytot), round(ytot.mean(),3), round(ytot.std(),3), round(ytot.median(),3)])
    stats= pd.DataFrame(stats_ampli_salle_list)
    stats.columns=['annee',  'salle', 'ampli', 'nbtotal', 'moyenne Gycm2', 'ecartType', 'median Gycm2']  

    ##table with mean, std, median, 75% percentile
    stats_cols=stats.columns[-7:]
    stats_ampli=pd.DataFrame(stats[stats_cols])
    fig4= go.Figure(go.Table(
                    columnwidth = [80,50],
                    header=dict(values=list(stats_cols),
                                fill_color='paleturquoise',
                                align='left'),
                    cells={"values": stats_ampli.T.values},
                                # fill_color='white',
                                  # align='left'
                                # visible = True
                                ))

                 
    fig4.update_layout(
            updatemenus=[   
                {
                    "y": 1 - (i / 5),
                    "buttons": [
                        {
                            "label": salle,
                            "method": "restyle",
                            "args": [
                                {
                                    "cells": {
                                        "values":  stats_ampli.loc[stats_ampli[menu].eq(salle)].T.values
                                          # if cat == "All"
                                          # else  stats_cat.loc[stats_cat[menu].eq(c)].T.values
                                    }
                                }
                            ],
                        }
                        for salle in stats_ampli[menu].unique().tolist()
                    ],   
                }
                for i, menu in enumerate(["salle"])
            ]
        )
    

    fig4.show() 

    return stats_ampli_salle