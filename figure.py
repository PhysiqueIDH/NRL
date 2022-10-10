# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 17:13:57 2022

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
   
    mat_y=[]
    mat_y=df[df['DATEINTERV'].dt.year==year] 
   
    fig3 = go.Figure()
    buttons1 = []
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
        for cat in cat_list:      
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
            
            # moy
            fig3.add_trace(
                go.Scatter(
                    x = mat['DATEINTERV'][mat['CATEGORY']==cat],
                    y = mat['DOSE Gycm2'][mat['CATEGORY']==cat],
                    # y = mat['TEMPS (s)'][mat['CATEGORY']==cat],
                    name = cat, visible = (i==1)
                    ))
        
        args = [False] * t_curves        
        args[l_curve:i*len(cat_list)+len(cat_list)] = [True] * len(cat_list)
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
            title_text = "DOSE $(Gycm^{2})$",
            # title_text = "temps (s)",
            title_standoff = 25)
            
    fig3.update_layout(
    autosize=False,
    width=1000,
    height=800,)

    fig3.show()   