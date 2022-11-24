# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 14:03:20 2021

@author: sorgato
"""
def dictionnairef (df):   
    from unidecode import unidecode
    import numpy as np
    import pandas as pd
    import difflib
    # df=dfTOT
    matrix = df.sort_values(by='DATEINTERV').reset_index(drop=True)
    matrix=df.dropna(subset = ['DOSE'])
    # dfRX=df.dropna(subset=['AMPLI']).reset_index(drop=True)
    # matrix.dropna(subset = ['DOSE'], inplace=True)
    types = list(matrix['MOTIF'])      
    types_corr= tuple(types)
    np.array(types)
    
    dictionn= pd.read_excel ('dictionnaire_interventions_bloc+laurent_pellet.xlsx', 'Feuil1')
    com=list(dictionn.loc[:,'com'])
    replace=list(dictionn.loc[:,'replace'])
    categ=list(dictionn.loc[:,'catégorie'])
    cond = list(dictionn.loc[:, 'condition'])

    types_corr=[]
    # i=0
    for i in range(0, len(types)):
        typ=types[i]
        # s=14
        ii=0
        if not pd.isna(typ):        
            if not isinstance(typ, float) or not typ.isdigit():                 
                for s in range(0, len(com)):                
                    if unidecode(com[s].lower()) in unidecode(typ.lower()) and ii==0:
                        ii+=1
                        if type(cond[s])==str:
                            if com[s] == 'boitier' and (len(set(matrix['NOMPRATICIEN'].iloc[i].split())&(set(cond[s].split())))!=0): #on va chercher à faire différence selon médecin
                                types_corr.append((typ, i, com[s], s, replace[s], categ[s]))
                        else:
                            types_corr.append((typ, i, com[s], s, replace[s], categ[s]))
                if ii==0:
                    types_corr.append((typ, i, 'lala', 'lala', 'lala'))                
            else:
                types_corr.append((typ, i, 'nan', 'nan', 'nan'))
        else:
            types_corr.append((typ, i, 'nan', 'nan', 'nan'))
                
    types_corr=np.array(types_corr)
    
    # # this option also works but is also longer!!
    # for i in range(0, len(types)):
    #     typ=types[i]
    #     if not pd.isna(typ):
    #         if not typ.isdigit():                
    #             s = com.index(difflib.get_close_matches(typ, com, len(com), 0)[0])
    #             if s:
    #                 types_corr.append((typ, i, com[s], replace[s], categ[s]))
    #             else:
    #                 types_corr.append((typ, i, 'lala', 'lala', 'lala'))           
    #     else:
    #         types_corr.append((typ, i, 'nan', 'nan', 'nan'))
                
    # types_corr=np.array(types_corr)
    
    # ceux qui n'ont pas trouvé leur place dans dictionnaire
    revoir = types_corr[np.array(np.where(types_corr[:,4] == 'lala')), :]
    revoir_uni=np.unique(revoir)
    # revoir_tout=matrix[np.array(np.where(types_corr[:,4] == 'lala')), :]
    # no_integers = np.delete(revoir_uni, np.where(revoir_uni[np.char.isdecimal(revoir_uni)].astype(int)))
    # dftest = pd.DataFrame(no_integers).T.transpose()
    # dftest.to_excel(excel_writer = "C:/test_NRI/spyder/test.xlsx")
    
       
    types_corr_uni=np.unique(types_corr[:,3])
    # types_corr_uni.to_excel("dic_net.xlsx")
                      
    # matrix['MOTIF_red']=types_corr[:,3]
    matrix['MOTIF_corr']=types_corr[:,3]
    matrix['CATEGORY']=types_corr[:,4]
    
    matrix['MOTIF_corr'][matrix['MOTIF']==matrix['MOTIF_corr']]= df['MOTIF']

    
    # Delete these row indexes from dataFrame
    indexNames = matrix[matrix['MOTIF_corr'] == 'lala'].index
    matrix.drop(indexNames , inplace=True)
    indexNames = matrix[matrix['MOTIF_corr'] == 'nan'].index
    matrix.drop(indexNames , inplace=True)
    indexNames = matrix[matrix['MOTIF_corr'] == 'Nan'].index
    matrix.drop(indexNames , inplace=True)    
    
    return matrix