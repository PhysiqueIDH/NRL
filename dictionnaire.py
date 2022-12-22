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
    # import progressbar

    matrix = df
    # matrix=df.dropna(subset = ['DOSE'])
    # dfRX=df.dropna(subset=['AMPLI']).reset_index(drop=True)
    # matrix.dropna(subset = ['DOSE'], inplace=True)
    types = list(matrix['MOTIF'])

    
    dictionn= pd.read_excel ('dictionnaire_interventions_bloc+laurent_pellet.xlsx', 'Feuil1')
    com = [item.lower() for item in list(dictionn.loc[:,'com'])]
    replace=list(dictionn.loc[:,'replace'])
    categ=list(dictionn.loc[:,'catégorie'])
    cond = list(dictionn.loc[:, 'condition'])

    types_corr=[]

    a=0
    for i in range(0, len(types)):
        s=[]
        typ=types[i]
        if not pd.isna(typ):        
            if not isinstance(typ, float) or not typ.isdigit():
                valr=difflib.get_close_matches(unidecode(typ.lower()), com, n=1, cutoff=0.6)
                if valr==[]:
                    valrr=difflib.get_close_matches(' '.join(unidecode(typ.lower()).split()[0:2]), com, n=1, cutoff=0.6)
                    if valrr==[] :
                        valrrr = difflib.get_close_matches(''.join(unidecode(typ.lower()).split()[0:1]), com, n=1, cutoff=0.7)
                        if valrrr==[] :
                            valrrrr = difflib.get_close_matches(''.join(unidecode(typ.lower()).split()[1:2]), com, n=1, cutoff=0.7)
                            if valrrrr==[] :
                                types_corr.append([typ, i, 'lala', 'lala', 'lala'])
                                s=[]
                            else:
                                s = com.index(str(valrrrr)[2:-2])
                        else:
                            s = com.index(str(valrrr)[2:-2])
                    else:
                        s=com.index(str(valrr)[2:-2])
                else:
                    s=com.index(str(valr)[2:-2])

                if s != []:
                    if type(cond[s])==str:
                        if com[s] == 'boitier':
                            ss = [index for index in range(len(com)) if com[index] == 'implant']
                            t=0
                            for index in ss:
                                if not pd.isna(cond[index]) and not isinstance(matrix['NOMPRATICIEN'].iloc[i], float):
                                    if len(set(matrix['NOMPRATICIEN'].iloc[i].split()) & (set(cond[index].split()))) != 0:
                                        types_corr.append([typ, i, com[index], replace[index], categ[index]])
                                        t=1
                                else:
                                    if pd.isna(cond[index]) and t==0:
                                        types_corr.append([typ, i, com[index], replace[index], categ[index]])

                        if com[s] == 'implant':
                            ss = [index for index in range(len(com)) if com[index] == 'implant']
                            t=0
                            for index in ss:
                                if not pd.isna(cond[index]) and not isinstance(matrix['NOMPRATICIEN'].iloc[i], float):
                                    if len(set(matrix['NOMPRATICIEN'].iloc[i].split()) & (set(cond[index].split()))) != 0:
                                        types_corr.append([typ, i, com[index], replace[index], categ[index]])
                                        t=1
                                else:
                                    if pd.isna(cond[index]) and t==0:
                                        types_corr.append([typ, i, com[index], replace[index], categ[index]])
                    else:
                        types_corr.append([typ, i, com[s], replace[s], categ[s]])

            else:
                types_corr.append([typ, i, 'nan', 'nan', 'nan'])
        else:
                types_corr.append([typ, i, 'nan', 'nan', 'nan'])

        if len(types_corr) != i+1:
            a+=1

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
    types_corrdf=pd.DataFrame(types_corr)
    # ceux qui n'ont pas trouvé leur place dans dictionnaire
    revoir = types_corrdf.loc[types_corrdf.iloc[:,4] == 'lala', :]
    revoir_uni=revoir.iloc[:,0].drop_duplicates()


    revoir_uni.to_excel('U:\\PYTHON_VSO\\NRLs\\EXTRACTION'+'\\revoir.xlsx', sheet_name='Feuil1')

    matrix['MOTIF_corr']=types_corrdf.iloc[:,3]
    matrix['CATEGORY']=types_corrdf.iloc[:,4]

    matrix.to_excel('U:\\PYTHON_VSO\\NRLs\\EXTRACTION'+'\\matrix.xlsx', sheet_name='Feuil1')
    types_corrdf.to_excel('U:\\PYTHON_VSO\\NRLs\\EXTRACTION' + '\\types_corr.xlsx', sheet_name='Feuil1')
    # Delete these row indexes from dataFrame
    indexNames = matrix[matrix['MOTIF_corr'] == 'lala'].index
    matrix.drop(indexNames , inplace=True)
    indexNames = matrix[matrix['MOTIF_corr'] == 'nan'].index
    matrix.drop(indexNames , inplace=True)
    indexNames = matrix[matrix['MOTIF_corr'] == 'Nan'].index
    matrix.drop(indexNames , inplace=True)    
    
    return matrix