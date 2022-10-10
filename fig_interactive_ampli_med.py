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
        
def fig_int_ampli_med (df, year):
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
    mat_y=mat_i[mat_i['MOTIF_corr']=='Cimentoplastie'] 
   
    fig3 = go.Figure()
    fig4 = go.Figure()
    stats_ampli_med = pd.DataFrame([], columns=['annee', 'ampli', 'medecin', 'nbtotal', 'Dose moy'])
    stats_ampli_med_list=[]
    
    
    buttons1 = []
    i = 0
    ampli_list = list(mat_y['AMPLI'].unique())  

    t_curves=0
    for ampli in ampli_list:
        mat=mat_y[mat_y['AMPLI']==ampli] 
        med_list = list(mat['NOMPRATICIEN'].unique()) 
        t_curves+=len(med_list)
    args = [False] * t_curves
       
    
    l_curve=0
    for ampli in ampli_list:

        mat=[]
        mat=mat_y[mat_y['AMPLI']==ampli]                    


        med_list = []
        med_list = list(mat['NOMPRATICIEN'].unique()) 
        for med in med_list:      
            matint=[]
            # yy=mat['DATEINTERV'][mat['NOMPRATICIEN']==med]
            # t=matint.dt.date.value_counts()
            # tch=pd.to_datetime(t.index[t>1])
            # for tst in matint:
            #     if tst in tch:
            #         st=matint[matint==tst]
            #         for j in range(0, len(st)):                        
            #             st.iloc[j]=pd.to_datetime(st.iloc[j] + pd.DateOffset(hour=j))                        
                    
            #         mat['DATEINTERV'].loc[st.index]=pd.to_datetime(st)                
            
            yy=mat['DOSE Gycm2'][mat['NOMPRATICIEN']==med]
            
            stats_ampli_med_list.append([year, ampli, med, len(yy), round(yy.mean(),3)])
            # , round(yy.mean(),3), round(yy.std(),3), round(yy.median(),3), round(np.percentile(yy, 75),3)])
            
            fig3.add_trace(
                go.Scatter(
                    x = mat['DATEINTERV'][mat['NOMPRATICIEN']==med],
                    y = yy,
                    # y = mat['TEMPS (s)'][mat['CATEGORY']==cat],
                    name = med, visible = (i==0)))
                    
            
            stats= pd.DataFrame(stats_ampli_med_list)
            stats.columns=['annee', 'ampli', 'medecin', 'nbtotal', 'Dose moy']        


        args = [False] * t_curves        
        args[l_curve:i*len(med_list)+len(med_list)] = [True] * len(med_list)
        # args[l_curve:len(cat_list)+l_curve] = [True] * len(cat_list) #also works
        #i is an iterable used to tell our "args" list which value to set to True
        i+=1
        l_curve+=len(med_list)

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
   

          
    fig3.update_layout(
    autosize=True,
    # width=1000,
    # height=800,
    title_text="Medecins " + str(year),
    title_x=0.5, 
    yaxis={'title':r'PDS (Gycm^2)'}
    )
    
    # fig3.update_yaxes(title=r'PDS (Gycm^2)')
   
            
    fig3.update_layout(
    autosize=False,
    width=1000,
    height=800)

    fig3.show()       
    
    ##table with mean, std, median, 75% percentile
    stats_cols=stats_ampli_med.columns[-4:]
    stats_med=pd.DataFrame(stats[stats_cols])
    fig4= go.Figure(go.Table(
                    columnwidth = [80,50],
                    header=dict(values=list(stats_cols),
                                fill_color='paleturquoise',
                                align='left'),
                    cells={"values": stats_med.T.values},
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
                                        "values":  stats_med.loc[stats_med[menu].eq(ampli)].T.values
                                          # if cat == "All"
                                         # else  stats_cat.loc[stats_cat[menu].eq(c)].T.values
                                    }
                                }
                            ],
                        }
                        for ampli in stats_med[menu].unique().tolist()
                    ],   
                }
                for i, menu in enumerate(["ampli"])
            ]
        )
    

    fig4.show() 

    return stats_med