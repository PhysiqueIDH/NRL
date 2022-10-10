# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 14:58:12 2022

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
        
def fig_int_int (df, year, column):
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
    mat_i=df[df['DATEINTERV'].dt.year==year] 
    # mat_i=mat_y[mat_y['MOTIF_corr']==column] 
    
    
    fig3 = go.Figure()
    fig4 = go.Figure()
    stats = pd.DataFrame([], columns=['annee', 'ampli', column, 'nbtotal', 'moyenne Gycm2', 'ecartType', 'median Gycm2', '75%centile'])
    stats_list=[]    

    
    
    buttons1 = []
    i = 0
    ampli_list = list(mat_i['AMPLI'].unique())  

    t_curves=0
    for ampli in ampli_list:
        mat=mat_i[mat_i['AMPLI']==ampli] 
        cat_list = list(mat[column].unique()) 
        t_curves+=len(cat_list)
    args = [False] * t_curves
       
    
    l_curve=0
    for ampli in ampli_list:

        mat=[]
        mat=mat_i[mat_i['AMPLI']==ampli]                    


        cat_list = []
        cat_list = list(mat[column].unique()) 
        for cat in cat_list:      
            matint=[]
            matint=mat['DATEINTERV'][mat[column]==cat]
            t=matint.dt.date.value_counts()
            tch=pd.to_datetime(t.index[t>1])
            for tst in matint:
                if tst in tch:
                    st=matint[matint==tst]
                    for j in range(0, len(st)):                        
                        st.iloc[j]=pd.to_datetime(st.iloc[j] + pd.DateOffset(hour=j))                        
                    
                    mat['DATEINTERV'].loc[st.index]=pd.to_datetime(st)                
            
            yy=mat['DOSE Gycm2'][mat[column]==cat]
            
            stats_list.append([year, ampli, cat, len(yy), round(yy.mean(),3), round(yy.std(),3), round(yy.median(),3), round(np.percentile(yy, 75),3)])
            
            fig3.add_trace(
                go.Scatter(
                    x = mat['DATEINTERV'][mat[column]==cat],
                    y = yy,
                    # y = mat['TEMPS (s)'][mat[column]==cat],
                    name = cat, visible = (i==0)))
                    
            
 

        args = [False] * t_curves        
        args[l_curve:i*len(cat_list)+len(cat_list)] = [True] * len(cat_list)
        # args[l_curve:len(cat_list)+l_curve] = [True] * len(cat_list) #also works
        #i is an iterable used to tell our "args" list which value to set to True
        i+=1
        l_curve+=len(cat_list)

        button1 = dict(label = ampli,
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
            title_text = "PDS (Gycm^2)",
            # title_text = "temps (s)",
            title_standoff = 25)
    
      
    fig3.update_layout(
    autosize=True,
    # width=1000,
    # height=800,
    title_text="NRL année " + str(year),
    title_x=0.5)
            
    fig3.update_layout(
    autosize=False,
    width=1000,
    height=800)

    fig3.show()       
    
    ytot=mat_i['DOSE Gycm2']
    stats_list.append([year, 'TOTAL', cat, len(ytot), round(ytot.mean(),3), round(ytot.std(),3), round(ytot.median(),3), round(np.percentile(ytot, 75),3)])
    stats= pd.DataFrame(stats_list)
    stats.columns=['annee', 'ampli', column, 'nbtotal', 'moyenne Gycm2', 'ecartType', 'median', '75%centile']        

##table with mean, std, median, 75% percentile
    stats_cols=stats.columns[-8:]
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
    

    fig4.show() 

    return stats