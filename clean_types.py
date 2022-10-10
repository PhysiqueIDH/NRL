# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 15:13:21 2021

@author: sorgato
"""
def clean_typesf(look, replace, types_corr):
    import numpy as np
    # global types_corr
    # il faut les fusionner: dans types, plusieures sont les mêmes...
    # com = ['imento']
    look=str(com).strip('[]') 
    look=look[1:-1]
    result_set=[]
    str_match=[]
    s=types_corr[1]
    for s in types_corr:
        if look in s:
            str_match.append =s
            
            
    tra=list(types_corr).index(str_match)
    
    
    foo=1
    for foo in range(0, len(types_corr)): #foo is just a variable like i
    # str_match = [s for s in types_corr if types_corr[foo] in s] 
    
    
        res = [ele for ele in look if(ele in str(types_corr[foo]))]
        result_set.append(res)
        
#find index of non-empty item in list!
    i_emp=[i for i,x in enumerate(result_set) if x]

    # types_corr=np.array(types)
    types_corr[i_emp]=replace
    return np.array(types_corr)


    
def clean_typesff(typ, dictionn):
    import numpy as np
    com=list(dictionn.loc[:,'com'])
    categ=list(dictionn.loc[:,'catégorie'])
    s=0
    for s in range(0, len(com)):
        if com[s] in typ:
            ii=s
            types_corr=[com[s]
            