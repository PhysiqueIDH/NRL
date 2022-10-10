# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 11:57:22 2021

@author: sorgato
"""

def plot_interf(xx, yy, title):
    import plotly.graph_objects as go    
    import pandas as pd
    import plotly.io as pio
    # pio.renderers.default = 'svg'
    pio.renderers.default = 'browser'
    # %matplotlib inline
    # %matplotlib auto
    
    # # Load data
    # df = pd.read_csv(
    #     "https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv")
    # df.columns = [col.replace("AAPL.", "") for col in df.columns]
    
    # Create figure
    fig = go.Figure()    
    fig.add_trace(go.Scatter(x=list(xx), y=list(yy)))
    
    # def show_in_window(fig):
    #     import sys, os
    #     import plotly.offline
    #     from PyQt5.QtCore import QUrl
    #     from PyQt5.QtWebEngineWidgets import QWebEngineView
    #     from PyQt5.QtWidgets import QApplication
        
    #     plotly.offline.plot(fig, filename='name.html', auto_open=False)
        
    #     app = QApplication(sys.argv)
    #     web = QWebEngineView()
    #     file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "name.html"))
    #     web.load(QUrl.fromLocalFile(file_path))
    #     web.show()
    #     sys.exit(app.exec_())


    # show_in_window(fig)
    
    # Set title
    fig.update_layout(title_text=title)
    
    # Add range slider
    fig.update_layout(
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1,
                         label="1m",
                         step="month",
                         stepmode="backward"),
                    dict(count=6,
                         label="6m",
                         step="month",
                         stepmode="backward"),
                    dict(count=1,
                         label="YTD",
                         step="year",
                         stepmode="todate"),
                    dict(count=1,
                         label="1y",
                         step="year",
                         stepmode="backward"),
                    dict(step="all")
                ])
            ),
            rangeslider=dict(
                visible=True
            ),
            type="date"
        )
    )
    
    fig.show()
