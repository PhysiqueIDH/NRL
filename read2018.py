# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 19:38:28 2021

@author: sorgato
"""

def readf(fil2, sheet2):
    import os
    dire="U:\\PYTHON_VSO\\NRLs\\EXTRACTION\\2018"
    os.chdir(dire)
    
    import pandas as pd
    df= pd.read_excel(fil2, sheet2)    
  
    # from datetime import datetime
    
    import datetime
    time=df['Exposition']
    df['TEMPS (s)']=df['Exposition']
    i=0
    for t in time[:]:
        if isinstance(t, datetime.time) :
            secondes= t.hour * 60 + t.minute #dataframe le lit mal...en vrai t.hour=min et t.minute=seconds
            df.loc[i,'TEMPS (s)']= secondes
        i+=1
    
    
    from datetime import datetime
    # date=df['DateDebut']
    # df['DATEINTERV']=df['DateDebut']
    # i=0
    # for d in date[:]:
    #     df.loc[i,'DATEINTERV']=d.strftime("%d/%m/%y")
    #     i+=1
        
    df['DATEINTERV']=pd.to_datetime(df['DateDebut'], errors='coerce').dt.strftime('%d/%m/%y')

        
    df['AMPLI']=df['Ampli']
    df['DOSE']=df['Dose']
    df['MOTIF']=df['Motif']
    df['SALLE']=df['Salle']
    df['NOMPRATICIEN']=df['NomPraticien']
    df['IPP']=df['IdPatient']
    df['NOM']=df['Nom']
    
    df_top = list(df.columns) #list makes it list type to be able to find index
    i_nom=df_top.index('NOM')
    i_ipp=df_top.index('IPP')
    i_med=df_top.index('NOMPRATICIEN')
    i_salle=df_top.index('SALLE')    
    i_ampli = df_top.index('AMPLI')
    i_salle=df_top.index('SALLE')
    i_date = df_top.index('DATEINTERV')
    i_dose = df_top.index('DOSE')
    i_mot = df_top.index('MOTIF')
    i_sec = df_top.index('TEMPS (s)')
    
    return df,i_nom, i_ipp, i_med, i_date, i_salle, i_ampli, i_dose, i_sec, i_mot



