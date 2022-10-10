# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 12:04:57 2021

@author: sorgato
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 17:50:19 2021

@author: sorgato
"""


def plot_dataf(medecin, df):
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    import math
    from plot_inter import plot_interf
    import seaborn as sns
    from dose_corr import dose_corrf      
    
    matrix1 = df[df['NOMPRATICIEN'] == medecin[0]]
    for i in range(1, len(medecin)):
        matrix1 =matrix1.append(df[df['NOMPRATICIEN'] == medecin[i]], ignore_index=True)
    
    matrix = matrix1.sort_values(by='DATEINTERV').reset_index(drop=True)
    
    #trouver intervention irradiante
    matrix=matrix.dropna(subset=['AMPLI'])
    
    # types = list(matrix['MOTIF'].unique())
    types = list(matrix['MOTIF'])      
    types_corr= tuple(types)
    # np.array(types)
    
    
    dictionn= pd.read_excel ('dictionnaire_interventions_bloc+.xlsx', 'Feuil1')
    com=list(dictionn.loc[:,'com'])
    replace=list(dictionn.loc[:,'replace'])
    categ=list(dictionn.loc[:,'catégorie'])
    
    # from clean_types import clean_typesf
    # types_corr=np.array(types)
    # i=0
    # for i in range(0, len(dictionn)):
    #     com=list(dictionn.loc[i,'com'])
    #     com=[''.join(map(str, com))]
    #     replace= list(dictionn.loc[i,'replace'])
    #     replace=[''.join(map(str, replace))]
    #     types_corr =clean_typesf(com, replace, types_corr)
    #     i=+i   
           

    types_corr=[]
    # i=0
    for i in range(0, len(types)):
        typ=types[i]
        # s=14
        ii=0
        if not isinstance(typ, float):                 
            for s in range(0, len(com)):                
                if com[s] in typ and ii==0:
                    ii+=1
                    types_corr.append((typ, i, com[s], s, replace[s], categ[s]))
            if ii==0:
                types_corr.append((typ, i, 'lala', 0, 'lala', 'lala'))                
        else:
            types_corr.append((typ, i, 'nan', 0, 'nan', 'nan'))
                
    types_corr=np.array(types_corr)
    
    # ceux qui n'ont pas trouvé leur place dans dictionnaire
    revoir = types_corr[np.array(np.where(types_corr[:,5] == 'lala')), :]
    
    types_corr_uni=np.unique(types_corr[:,4])
    # types_corr_uni.to_excel("dic_net.xlsx")
                      
    matrix['MOTIF_red']=types_corr[:,3]
    matrix['MOTIF_corr']=types_corr[:,4]
    matrix['CATEGORY']=types_corr[:,5]
    recap=pd.DataFrame()
    recap['Intervention']=types_corr_uni
    recap['Mean PDS (µGy m2)']=np.zeros(len(types_corr_uni))
    recap['75% percentile (µGy m2)']=np.zeros(len(types_corr_uni))
    recap['Mean time (s)']=np.zeros(len(types_corr_uni))

    # i=0
    matrix['DOSE µGym2']=matrix['DOSE']
    for i in range(0, len(types_corr_uni)):       
        t = types_corr_uni[i]
        mat = matrix.loc[matrix['MOTIF_corr'] == t]
        im=matrix.index[matrix['MOTIF_corr'] == t].tolist()
       
        # mat2 = mat['DOSE'].fillna('0').astype(float)  # replace nan by 0
        # mat_dose = [float('nan') if x == 0 else x for x in mat2]  
        ampli = [str(x) for x in mat['AMPLI']][0]
        idc=dose_corr(ampli)               
        matrix['DOSE µGym2'][im]=mat['DOSE']*idc #µGym2  
        mat_dose = mat['DOSE']*idc #µGym2        
        mat_time = mat['TEMPS (s)']
        # pd.plotting.register_matplotlib_converters()
        
        # # try interactive plot: à faire
        # # xx=mat['DATEINTERV']
        # # yy= mat1
        # # title=t        
        # # plot_interf(mat['DATEINTERV'], mat1, t)
        # plt.figure()
        # plt.plot(mat['DATEINTERV'], matrix['DOSE µGym2'][im], 'ro')
        # plt.ylabel('PDS(µGy m2)')
        # plt.title(t)
        # plt.show()
        
        #calculate mean, 75% dose and time
        recap['Mean PDS (µGy m2)'][i]=round(np.nanmean(mat_dose), 2)
        recap['75% percentile (µGy m2)'][i]=round(np.nanpercentile(mat_dose, 50), 2)
        recap['Mean time (s)'][i]=round(np.mean(mat_time), 2)
        
        
    # plot histogram with mean PDS        # 
    plots = sns.barplot(x="Intervention", y="Mean PDS (µGy m2)", data=recap)
    plt.ylabel("PDS (µGy m2)")
    # plt.title(medecin)
    n=range(0, len(recap['Intervention']))
    for i in range(len(n)):
        plt.annotate(str(recap['Mean PDS (µGy m2)'][i]), xy=(n[i],recap['Mean PDS (µGy m2)'][i]), ha='center', va='bottom')
    plt.show()

    
    plt.figure()
    plots = sns.barplot(x="Intervention", y="Mean time (s)", data=recap)
    plt.ylabel("Temps (s)")
    # plt.title(medecin)
    n=range(0, len(recap['Intervention']))
    for i in range(len(n)):
        plt.annotate(str(recap['Mean time (s)'][i]), xy=(n[i],recap['Mean time (s)'][i]), ha='center', va='bottom')
    plt.show()
   
    
