# -*- coding: utf-8 -*-
"""
Cette fonction nettoie la BDD.
"""

def mergef(fil, sheet):
    # global df, i_dose, i_sec, i_min, i_mot
    # # This is a code to import data and merge/correct before analyzing it
    # import os
    # prevdir = os.getcwd()
    # #os.chdir(prevdir) this is to go to prevdir
    
    import pandas as pd
    df= pd.read_excel (fil, sheet)
    
    # import os
    # dire="N:\\Themes\\Radioprotection GHM\\PYTHON_VSO\\NRLs\\EXTRACTION\\2019-2022"
    # dir="C:\\test_NRI\\spyder" 
    # os.chdir(dire)
    
  
    
    #trouver colonne de PDS
    df_top = list(df.columns) #list makes it list type to be able to find index
    col_dose_names=["dose", "DOSE", "dos", "D", "Evénement conclusion.Dose totale"] #list of possible words to find for dose
    both = set(df_top).intersection(col_dose_names)
    i_dose = [df_top.index(x) for x in both] #index of column name Dose
   # 'Gycm2' en hemolia (DoseTotale) et Gym2 en careanalytics
   # 'mGy' en hemolia (AirKerma) et Gy en careanalytics
    if 'Evénement conclusion.Dose totale' in df_top:
        df['DOSE']=df['Evénement conclusion.Dose totale']
        # i_dose=df_top.index('DOSE')
    
    #TEMPS
    #trouver colonne de secondes et fusioner dans Secondes
    col_sec_names=["EXPOSITIONSecondes", "EXPOSITIONSECONDES", "Evénement conclusion.Temps de scopie (sec)"]
    both = set(df_top).intersection(col_sec_names)
    i_sec = [df_top.index(x) for x in both] #index of column name seconds
    if 'EXPOSITIONSecondes' in df_top:
        Sec_empty = df['EXPOSITIONSecondes'].isnull()
        SEC_notempty = df['EXPOSITIONSECONDES'].notnull()
        #find indexes to merge
        i_merge=[i for i, x in enumerate(Sec_empty & SEC_notempty) if x]
        #merge
        df.loc[i_merge, 'EXPOSITIONSecondes']=df.loc[i_merge, 'EXPOSITIONSECONDES']
      
    # df = df.drop(labels='EXPOSITIONSECONDES', axis=1) #erase
    
    #trouver colonne de minutes et fusioner dans Minutes
    col_min_names=["EXPOSITIONMinutes", "EXPOSITIONMINUTES"]
    both = set(df_top).intersection(col_min_names)
    i_min = [df_top.index(x) for x in both] #index of column name seconds
    if 'EXPOSITIONMinutes' in df_top:
        Min_empty = df['EXPOSITIONMinutes'].isnull()
        MIN_notempty = df['EXPOSITIONMINUTES'].notnull()
        #find indexes to merge
        i_mergem=[i for i, x in enumerate(Min_empty & MIN_notempty) if x]
        #merge
        df.loc[i_mergem, 'EXPOSITIONMinutes']=df.loc[i_mergem, 'EXPOSITIONMINUTES']
        # df = df.drop(labels='EXPOSITIONMINUTES', axis=1) #erase
    
        df.loc[:,'TEMPS (s)']=df.loc[:, 'EXPOSITIONMinutes']*60+df.loc[:,'EXPOSITIONSecondes']
    
    if 'Evénement conclusion.Temps de scopie (sec)' in df_top:
        df.loc[:,'TEMPS (s)']=df.loc[:, 'Evénement conclusion.Temps de scopie (sec)']

    df_top = list(df.columns) #list makes it list type to be able to find index
    i_secT = df_top.index('TEMPS (s)')
    
    #trouver colonne de type exposition
    col_mot_names=["MODELELIB", "MOTIF", "Procédure.Titre 1"]
    both = set(df_top).intersection(col_mot_names)
    i_mot = [df_top.index(x) for x in both] #index of column name seconds
    if 'MOTIF' in df_top:
        Mot_empty = df['MOTIF'].isnull()
        if 'MODELELIB' in df_top:
            MOT_notempty = df['MODELELIB'].notnull()
            #find indexes to merge
            i_mergemo=[i for i, x in enumerate(Mot_empty & MOT_notempty) if x]
            #merge
            df.loc[i_mergemo, 'MOTIF']=df.loc[i_mergemo, 'MODELELIB']



    if 'Procédure.Titre 1' in df_top:
        df['Procédure.Titre 1'][df['Procédure.Titre 2']=='CTO']= df['Procédure.Titre 2']
        df['Procédure.Titre 1'][df['Procédure.Titre 2']=='OCT']= df['Procédure.Titre 2']
        df['MOTIF']=df['Procédure.Titre 1']

                
    if 'DATEINTERV' in df_top:
        df['DATEINTERV']=pd.to_datetime(df['DATEINTERV'], errors='coerce').dt.strftime('%d/%m/%y')
    if 'Procédure.Date de la procédure' in df_top:
        df['DATEINTERV']=pd.to_datetime(df['Procédure.Date de la procédure'], errors='coerce').dt.strftime('%d/%m/%y')

    
    if 'Procédure.Salle' in df_top:
        df['SALLE']=df['Procédure.Salle']
        df['AMPLI']=df['Procédure.Salle']
    
    df['AMPLI'].loc[(df['SALLE'] =='3-BERLIOZ')] = '3-BERLIOZ'
    df['AMPLI'].loc[(df['SALLE'] =='2-STENDHAL')] = '2-STENDHAL'
    df['AMPLI'].loc[(df['SALLE'] =='1-CHAMPO')] = '1-CHAMPO'


    if 'Procédure.Opérateur' in df_top:
        df['NOMPRATICIEN']=df['Procédure.Opérateur']
        
    if 'Procédure.Nom de famille' in df_top:
        df['NOM']=df['Procédure.Nom de famille']

    if 'Procédure.Procédure.ID' in df_top:
        df['IPP']=df['Procédure.Procédure.ID']
        
    
    df_top = list(df.columns)
    i_dose = df_top.index('DOSE')  
    i_mot = df_top.index('MOTIF')  
    i_salle=df_top.index('SALLE')   
    i_ampli= df_top.index('AMPLI')       
    i_ipp= df_top.index('IPP')
    i_nom= df_top.index('NOM')
    i_med= df_top.index('NOMPRATICIEN')
    i_date = df_top.index('DATEINTERV')
    
    df['DOSE']=[float(str(i).replace(",", ".")) for i in df['DOSE']]

    df = df.iloc[1: , :]
    
    return df, i_nom, i_ipp, i_med, i_date, i_salle, i_ampli, i_dose, i_secT, i_mot
    
    
    
    #essayer de récupérer infos dans commentaires...trop dur! ceci marche pour dataframe
    # m = df['COMMENTAIRE'].str.contains('s|sec|secondes|min', na=False) #mettre TRUE pour cellules qui contiennent ce texte et FALSE pour les autres
    # ind=[i for i, x in enumerate(m) if x] # trouver index des cellules TRUE dans m
    
    ## import numpy as np. ceci marche car s'est une serie de strings, mais pas pour dataframe!
    ## A = ['apple', 'orange', 'apple', 'banana']
    ## arr_mask = np.where(np.array(A) == 'apple',True,False)
    ## arr_index = np.arange(0, len(A))[arr_mask]
    
    
    
    
    
    
    
    
    
    # #example
    # dfr = pd.DataFrame({'A': [0, 0, 2, 1], 'B': [1,2,3,4]})
    # t = [dfr.loc[lambda dfr: dfr['A'] == 1]]
    # t
    
    # f_str=df.applymap(lambda x: type(x) == str)
    # f_str()
    # ind=df(().contains('dose', na=False)
    # sub ='dose'
    # # creating and passing series to new column
    # df["Indexes"]= df.str.find(sub)
    
    # s = pd.Series(['foo', 'foobar', np.nan, 'bar', 'baz', 123])
    # ind=s.str.contains('foo|bar', na=False)
    # ind
    
    
    
    # both = set(df).intersection(col_dose_names)
    # i = [df.index(x) for x in both] #index of column name Dose
    # i
    
    
