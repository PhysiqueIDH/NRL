# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 10:09:23 2022

@author: sorgato
"""
def preparation():
    # %autoreload
    import os
    dir="U:\\PYTHON_VSO\\NRLs\\Fork\\NRL"
    # dir="C:\\test_NRI\\spyder" 
    os.chdir(dir)
    # #A UTILISER POUR AVOIR UN SEUL EXCEL EXTRACTION
    # # avant de faire marcher le code suivant, s'assurer que dans le fichier N:\\Themes\\Radioprotection GHM\\PYTHON_VSO\\NRLs\\EXTRACTION, 
    # #tous les fichiers excels y sont. Ce code va fusioner tous les excels en un: "All2019-2022.xlsx"
    # from fusion_EXTRACTION import fusion_extractionf
    # fusion_extractionf()
    # # import os
    # dir="U:\\PYTHON_VSO\\NRLs\\spyder"
    
    from merge import mergef
    # # global df, dire, i_dose, i_sec, i_min, i_mot
    dire="U:\\PYTHON_VSO\\NRLs\\EXTRACTION\\2019-2022"
    os.chdir(dire)
    fil='All2019-2022.xlsx'
    sheet='Sheet1'
    [df1, i_nom1, i_ipp1, i_med1, i_date1, i_salle1, i_ampli1, i_dose1, i_sec1, i_mot1]=mergef(fil, sheet)
    idf1=[i_nom1, i_ipp1, i_med1, i_date1, i_salle1, i_ampli1, i_dose1, i_sec1, i_mot1]
    
    os.chdir(dir)
    from read2018 import readf
    dire="U:\\PYTHON_VSO\\NRLs\\EXTRACTION\\2018"
    os.chdir(dire)
    fil2='GENERAL2018TW.xlsx'
    sheet2='RAW DATA'
    [df2, i_nom2, i_ipp2, i_med2, i_date2, i_salle2, i_ampli2, i_dose2, i_sec2, i_mot2]=readf(fil2, sheet2)
    idf2=[i_nom2, i_ipp2, i_med2, i_date2, i_salle2, i_ampli2, i_dose2, i_sec2, i_mot2]
    
 #------------CICI
    import os
    dire="U:\\PYTHON_VSO\\NRLs\\EXTRACTION\CICI"
    # dire='C:\\test_NRI\\CICI'
    os.chdir(dire)
    fil3='2014-2022.xlsx'
    sheet3='NRL Tous'
    [df3, i_nom3, i_ipp3, i_med3, i_date3, i_salle3, i_ampli3, i_dose3, i_sec3, i_mot3]=mergef(fil3, sheet3) #!! NE MARCHE PAS!! Dose Champollion vide???
    idf3=[i_nom3, i_ipp3, i_med3, i_date3, i_salle3, i_ampli3, i_dose3, i_sec3, i_mot3]
   
 
 
 #--------------

    #fusionner df1 2019-2021 et df2 2018 
    dfTOT1=df1.iloc[:, idf1].append(df2.iloc[:, idf2])
    dfTOT2=dfTOT1.append(df3.iloc[:, idf3])
    dfTOT=dfTOT2

    
  
    #nettoyer doublons: ok
    import datetime
    import pandas as pd
    dfTOT['DATEINTERV']=pd.to_datetime(dfTOT['DATEINTERV'], infer_datetime_format=True)
    dfTOT = dfTOT.sort_values(by='DATEINTERV').reset_index(drop=True)
    # dfTOT=dfTOT.drop("Unnamed: 0",axis=1)
    
    import os
    dir="U:\\PYTHON_VSO\\NRLs\\EXTRACTION"
    # dir="C:\\test_NRI\\spyder" 
    os.chdir(dir)
    
    from dictionnaire import dictionnairef
    dfTOTdic=dictionnairef(dfTOT)
    dfTOT=dfTOTdic
    
    #corriger la dose des différentes unités
    import numpy as np
    from dose_corr import dose_corrf      
    from ampli_corr import ampli_corrf 
    from salle_corr import salle_corrf 
    dfTOT['DOSE Gycm2']=dfTOT['DOSE']
    dfTOT=dfTOT.dropna(subset = ['DOSE'])
    dfTOT['AMPLI']=dfTOT['AMPLI'].replace(to_replace="Pas d'amplificateur", value=np.nan)
    amplis=np.unique(dfTOT['AMPLI'].astype(str))
    salle=np.unique(dfTOT['SALLE'].astype(str))
    for a in amplis:
        idc=dose_corrf(a)   
        im=dfTOT.index[dfTOT['AMPLI'] == a].tolist()          
        dfTOT['DOSE Gycm2'][im]=dfTOT['DOSE'][im]*idc #Gycm2  
        dfTOT['AMPLI']=dfTOT['AMPLI'].replace(to_replace=a, value=ampli_corrf(a))
    for s in salle:          
        dfTOT['SALLE']=dfTOT['SALLE'].replace(to_replace=s, value=salle_corrf(s))    
    
    sallec=np.unique(dfTOT['AMPLI'].astype(str))
    
    dfTOT.loc[dfTOT['SALLE']=='Berlioz','AMPLI']='Berlioz'
    dfTOT.loc[dfTOT['SALLE']=='Champollion','AMPLI']='Champollion'
    dfTOT.loc[dfTOT['SALLE']=='Stendhal','AMPLI']='Stendhal'
            
    
       
    dire="N:\\Themes\\Radioprotection GHM\\PYTHON_VSO\\NRLs\\EXTRACTION"
    os.chdir(dire)
    dfTOT.to_excel("ALL_2014-2022.xlsx")
    # dfTOT.to_excel("ALL_BLOC_CICI_2018-2022.xlsx")
       
    # import os
    # dire="N:\\Themes\\Radioprotection GHM\\PYTHON_VSO\\NRLs\\EXTRACTION"
    # os.chdir(dire)
    # fil='ALL_2018-2019-2022_RX.xlsx'
    # sheet='Sheet1'
    # import pandas as pd
    # df= pd.read_excel (fil, sheet)
    
    
    # #trouver intervention irradiantes seulement
    # dfTOT=dfTOT.drop("Unnamed: 0",axis=1)
    dfRX=dfTOT.dropna(subset=['DOSE']).reset_index(drop=True)
    dfRX.to_excel("ALL_BLOC_CICI_2014-2022_RX.xlsx")
    
    # from plot_interv import plot_intervf

    
    
    return dfRX