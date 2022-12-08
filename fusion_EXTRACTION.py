# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 16:18:44 2021

@author: sorgato
"""
def fusion_extractionf():
    import os
    dir="U:\\PYTHON_VSO\\NRLs\\EXTRACTION\\2019-2022"
    os.chdir(dir)
    import pandas as pd
    # get data file names
    path = os.getcwd()
    files = os.listdir(path)
    # files
    files_xls = [f for f in files if f[-4:] == 'xlsx']

    # f=files_xls[23]

    for f in files_xls[:]:
        if not f[0].isdigit():
            files_xls.remove(f)
        
    df = pd.DataFrame()

    for f in files_xls[:]:
        data = pd.read_excel(f, 'Feuil1')
        df = df.append(data)        

    # dire="N:\\Themes\\Radioprotection GHM\\PYTHON_VSO\\EXTRACTION\\2019-2021"
    # os.chdir(dire)
    
    df.to_excel("All2019-2022.xlsx")
