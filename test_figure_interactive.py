  
    # from dash import Dash, html, dcc, Input, Output
    # import plotly.express as px

# JE SUIS RESTEE LA!!!
   #add time info selection
    # https://dash.plotly.com/interactive-graphing
    

        
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


    buttons1 = []
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
        args2=[]
        for cat in cat_list:  
            yy=[]
            c+=1
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
            
            stats_list.append([year, ampli, cat, len(yy), yy.mean(), yy.std()])
            
            fig3.add_trace(
                go.Scatter(
                    x = mat['DATEINTERV'][mat['CATEGORY']==cat],
                    y = yy,
                    # y = mat['TEMPS (s)'][mat['CATEGORY']==cat],
                    name = cat, visible = True), 
                    row=1, col=1)
            
        stats= pd.DataFrame(stats_list)
        stats.columns=['annee', 'ampli', 'categorie', 'nbtotal', 'moyenne', 'ecartType']
        stats_cat=stats.iloc[l_curve:len(cat_list)+l_curve]
        stats_cols=stats_cat.columns[-5:]
# je suis làààààà      https://stackoverflow.com/questions/69568250/interactive-filtering-data-table-in-plotly-by-using-a-dropdown 
        fig3.add_trace(go.Table(
                columnwidth = [80,50],
                header=dict(values=list(stats_cols),
                            fill_color='paleturquoise',
                            align='left'),
                cells=dict(values=[stats[xx] for xx in stats_cols],
                            fill_color='white',
                            align='left'),
                name = cat, visible = True), row=1, col=2)
                
        args2.append([ {"cells": {"values": stats_cat.T.values } } ])                        


                        
                   


       # {"values": [scores[x] for x in scores_cols]   
        # stats= pd.DataFrame(stats_list)
        # stats.columns=['annee', 'ampli', 'categorie', 'nbtotal', 'moyenne', 'ecartType']

        args = [False] * t_curves        
        args[l_curve:i*len(cat_list)+len(cat_list)] = [True] * len(cat_list)
        #i is an iterable used to tell our "args" list which value to set to True

        # button1 = dict(label = ampli,
        #               method = "update",
        #               args=[{"visible": args}])
        # buttons1.append(button1)

        button2 = dict(label = ampli,
                      method = "update",
                      args=[{"visible": args}])
        buttons2.append(button2)

        
        # args2 = [False] * t_curves         
        # args2[l_curve:len(cat_list)+l_curve] = [True] * len(cat_list)

        i+=1
        l_curve+=len(cat_list)

                    
                
    fig3.update_layout(updatemenus=[dict(active=0,
                          type="dropdown",
                          buttons=buttons2,
                          x = 0,
                          y = 1.1,
                          xanchor = 'left',
                          yanchor = 'bottom'
                          )])
    
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
   

    fig3.update_yaxes(title_text="DOSE $(Gycm^{2})$", row=1, col=1)

    fig3.update_layout(
    autosize=True,
    # width=1000,
    # height=800,
    title_text="NRL année " + str(year),
    title_x=0.5)
    
    fig3.show()   
    


