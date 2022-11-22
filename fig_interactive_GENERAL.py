# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 16:14:39 2022

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
        
def fig_int_GENERAL(df, year, param1, param2, interv=None):
    import plotly.graph_objs as go
    import plotly.io as pio
    import sys
    import numpy as np
    from datetime import timedelta
    from datetime import datetime
    import pandas as pd
    from plotly.subplots import make_subplots
    # pio.renderers.default = 'svg'
    pio.renderers.default = 'browser'

    # YEAR
    yearmin = min(year)
    yearmax = max(year)
    mat_yy = df[df['DATEINTERV'].dt.year >= yearmin]
    mat_y = mat_yy[mat_yy['DATEINTERV'].dt.year <= yearmax]

    # PARAMETERS
    def switch(parameter):
        if parameter == "AMPLI":
            return "AMPLI"
        elif parameter == "MOTIF_corr":
            return "MOTIF_corr"
        elif parameter == "CATEGORY":
            return "CATEGORY"
        elif parameter == "SALLE":
            return "SALLE"
        elif parameter == "NOMPRATICIEN":
            return "NOMPRATICIEN"


    if interv!=None:
        mat_i = mat_y[mat_y['MOTIF_corr'] == interv]
    else:
        mat_i = mat_y

# preparation
    fig3 = go.Figure()
    fig2 = go.Figure()
    fig4 = go.Figure()

    stats= pd.DataFrame([], columns=['Annee', switch(param1), switch(param2), 'Nbtotal', 'PKS_moyen(Gycm2)', 'EcartType(Gycm2)','Median(Gycm2)', 'Temps_moyen(s)', 'EcartType(s)','Median(s)'])

    stats_list = []
    stats_list1 = []
    buttons1 = []
    i = 0
    button_l = list(mat_i[switch(param1)].unique())
    button_list = list(filter(lambda x: str(x) != 'nan' and str(x) != 'null', button_l))

    t_curves = 0
    for button in button_list:
        mat = mat_i[mat_i[switch(param1)] == button]
        legend_list = list(mat[switch(param2)].unique())
        t_curves += len(legend_list)
    args = [False] * t_curves

    l_curve = 0
    for button in button_list:

        mat = []
        mat = mat_i[mat_i[switch(param1)] == button]


        legend_l = list(mat[switch(param2)].unique())
        legend_list = list(filter(lambda x: str(x) != 'nan' and str(x) != 'null', legend_l))
        for leg in legend_list:
            matint = []
            matint = mat['DATEINTERV'][mat[switch(param2)] == leg]
            t = matint.dt.date.value_counts()
            tch = pd.to_datetime(t.index[t > 1])
            for tst in matint:
                if tst in tch:
                    st = matint[matint == tst]
                    for j in range(0, len(st)):
                        st.iloc[j] = pd.to_datetime(st.iloc[j] + pd.DateOffset(hour=j))

                    mat['DATEINTERV'].loc[st.index] = pd.to_datetime(st)

            yy = mat['DOSE Gycm2'][mat[switch(param2)] == leg]
            tt = mat['TEMPS (s)'][mat[switch(param2)] == leg]

            stats_list.append(
                [year, button, leg, len(yy), round(yy.mean(), 3), round(yy.std(), 3), round(yy.median(), 3), round(tt.mean(), 3), round(tt.std(), 3), round(tt.median(), 3)])
            stats_list1.append(
                [year, button, leg, len(yy), round(yy.mean(), 3), round(yy.std(), 3), round(yy.median(), 3), round(tt.mean(), 3), round(tt.std(), 3), round(tt.median(), 3)])

            fig3.add_trace(
                go.Scatter(
                    x=mat['DATEINTERV'][mat[switch(param2)] == leg],
                    y=yy,
                    # y = mat['TEMPS (s)'][mat[switch(param2)]==leg],
                    # name = [leg, mat['IPP'][mat[switch(param2)]==leg]], visible = (i==1)))
                    name=leg, visible=(i == 0)))
            fig2.add_trace(
                go.Scatter(
                    x=mat['DATEINTERV'][mat[switch(param2)] == leg],
                    y=tt,
                    name=leg, visible=(i == 0)))

        args = [False] * t_curves
        args[l_curve:i * len(legend_list) + len(legend_list)] = [True] * len(legend_list)
        # args[l_curve:len(legend_list)+l_curve] = [True] * len(legend_list) #also works
        # i is an iterable used to tell our "args" list which value to set to True
        i += 1
        l_curve += len(legend_list)

        button1 = dict(label=button,
                       method="update",
                       args=[{"visible": args}])
        buttons1.append(button1)
        ytot = mat['DOSE Gycm2']
        ttot = mat['TEMPS (s)']
        stats_list.append([year, button, 'TOTAL', len(ytot), round(ytot.mean(), 3), round(ytot.std(), 3), round(ytot.median(), 3),round(ttot.mean(), 3), round(ttot.std(), 3), round(ttot.median(), 3)])


    fig3.update_layout(updatemenus=[dict(active=0,
                                         type="dropdown",
                                         buttons=buttons1,
                                         x=0,
                                         y=1.1,
                                         xanchor='left',
                                         yanchor='bottom'
                                         ),
                                    ])

    fig3.update_yaxes(
        title_text="PDS (Gycm2=100µGym2)",
        # title_text = "temps (s)",
        title_standoff=25)

    fig3.update_layout(
        autosize=True,
        # width=1000,
        # height=800,
        title_text="NRL année " + str(year) + ', ',
        title_x=0.5)

    fig3.update_layout(
        autosize=False,
        width=1000,
        height=800)

    fig3.show()

    fig2.update_layout(updatemenus=[dict(active=0,
                                         type="dropdown",
                                         buttons=buttons1,
                                         x=0,
                                         y=1.1,
                                         xanchor='left',
                                         yanchor='bottom'
                                         ),
                                    ])

    fig2.update_yaxes(
        title_text="TEMPS (s)",
        title_standoff=25)

    fig2.update_layout(
        autosize=True,
        # width=1000,
        # height=800,
        title_text="NRL année " + str(year) + ', ',
        title_x=0.5)

    fig2.update_layout(
        autosize=False,
        width=1000,
        height=800)

    fig2.show()


    stats= pd.DataFrame(stats_list)
    stats.columns = ['Annee', switch(param1), switch(param2), 'Nbtotal', 'PKS_moyen(Gycm2)', 'EcartType(Gycm2)','Median(Gycm2)', 'Temps_moyen(s)', 'EcartType(s)','Median(s)']
    stats1=pd.DataFrame(stats_list1)
    stats1.columns = ['Annee', switch(param1), switch(param2), 'Nbtotal', 'PKS_moyen(Gycm2)', 'EcartType(Gycm2)','Median(Gycm2)', 'Temps_moyen(s)', 'EcartType(s)','Median(s)']
    ##table with mean, std, median, 75% percentile
    stats_cols = stats.columns[-11:]
    stats_leg = pd.DataFrame(stats[stats_cols])
    fig4 = go.Figure(go.Table(
        columnwidth=[80, 50],
        header=dict(values=list(stats_cols),
                    fill_color='paleturquoise',
                    align='left'),
        cells={"values": stats_leg.T.values},
    ))

    fig4.update_layout(
        updatemenus=[
            {
                "y": 1 - (i / 5),
                "buttons": [
                    {
                        "label": button,
                        "method": "restyle",
                        "args": [
                            {
                                "cells": {
                                    "values": stats_leg.loc[stats_leg[menu].eq(button)].T.values
                                    # if leg == "All"
                                    # else  stats_leg.loc[stats_leg[menu].eq(c)].T.values
                                }
                            }
                        ],
                    }
                    for button in stats_leg[menu].unique().tolist()
                ],
            }
            for i, menu in enumerate([switch(param1)])
        ]
    )

    fig4.show()

    fig2.write_html(sys.path[0] + "\\results\\" + switch(param1) + "-" + switch(param2) + "\\" + str(yearmin) + "TEMPS.html")
    fig3.write_html(sys.path[0]+"\\results\\"+switch(param1)+"-"+switch(param2)+"\\"+str(yearmin)+"PKS.html")
    fig4.write_html(sys.path[0]+"\\results\\"+switch(param1)+"-"+switch(param2)+"\\"+str(yearmin)+"_stats.html")
    stats1.to_excel(sys.path[0]+"\\results\\"+switch(param1)+"-"+switch(param2)+"\\"+str(yearmin)+"_stats.xlsx", sheet_name='Feuil1')

    return stats1