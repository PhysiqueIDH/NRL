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
        
def fig_int_GENERAL (df, year, param1, param2, interv=None):
    import plotly.graph_objs as go
    import plotly.io as pio
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
    fig4 = go.Figure()

    stats= pd.DataFrame([], columns=['Annee', switch(param1), switch(param2), 'Nbtotal', 'Moyenne Gycm2', 'EcartType', 'Median Gycm2'])
                        # , '75%centile'])
    stats_list = []

    buttons1 = []
    i = 0
    button_list = list(mat_i[switch(param1)].unique())

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

        legend_list = []
        legend_list = list(mat[switch(param2)].unique())
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

            stats_list.append(
                [year, button, leg, len(yy), round(yy.mean(), 3), round(yy.std(), 3), round(yy.median(), 3)])
                 # , round(np.percentile(yy, 75), 3)])

            fig3.add_trace(
                go.Scatter(
                    x=mat['DATEINTERV'][mat[switch(param2)] == leg],
                    y=yy,
                    # y = mat['TEMPS (s)'][mat[switch(param2)]==leg],
                    # name = [leg, mat['IPP'][mat[switch(param2)]==leg]], visible = (i==1)))
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

    # ytot = mat['DOSE Gycm2']
    # stats_list.append([year, button, 'TOTAL', len(ytot), round(ytot.mean(), 3), round(ytot.std(), 3), round(ytot.median(), 3),
    #      round(np.percentile(ytot, 75), 3)])
    stats= pd.DataFrame(stats_list)
    stats.columns = ['Annee', switch(param1), switch(param2), 'Nbtotal', 'Moyenne Gycm2', 'EcartType','Median Gycm2']
    # , '75%centile']

    ##table with mean, std, median, 75% percentile
    stats_cols = stats.columns[-8:]
    stats_leg = pd.DataFrame(stats[stats_cols])
    fig4 = go.Figure(go.Table(
        columnwidth=[80, 50],
        header=dict(values=list(stats_cols),
                    fill_color='paleturquoise',
                    align='left'),
        cells={"values": stats_leg.T.values},
        # fill_color='white',
        # align='left'
        # visible = True
    ))

    # fig3 = go.Figure(go.Table(header={"values": stats_cols}, cells={"values": stats_leg.T.values}))
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

    fig3.write_html("N:\\Themes\\Radioprotection GHM\\PYTHON_VSO\\NRLs\\figures\\" +switch(param1)+"-"+switch(param2)+".html")
    fig4.write_html("N:\\Themes\\Radioprotection GHM\\PYTHON_VSO\\NRLs\\figures\\" +switch(param1)+"-"+switch(param2)+ "_stats.html")

    return stats 