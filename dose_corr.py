# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 17:48:29 2021

@author: sorgato
"""

def dose_corrf(ampli): 
    # import pandas as pd
    # ampli=pd.Series(ampli)  
    switcher={
        # '21    SIEM_CIOS\nName: AMPLI, dtype: object': lambda:1,#µGym2
        'SIEM_CIOS':lambda:0.01,#1µGym2=0.01Gycm2        'Siemens (µGym²)
        'CIOS Fusion (µGym²)':lambda:0.01,#1µGym2=0.01Gycm2 
        'CIOS':lambda:0.01,#1µGym2=0.01Gycm2 
        'Siemens (µGym²)':lambda:0.01,#1µGym2=0.01Gycm2 
        'SIEM_VARIC':lambda:0.01,#1cGycm2=0.01Gycm2 
        'VARIC':lambda:0.01,#1cGycm2=0.01Gycm2 
        'Siemens Varic (cGycm²)':lambda:0.01,#1cGycm2=0.01Gycm2 
        'ORTHOSCAN':lambda:0.001, #1mGycm2=0.001Gycm2
        'Orthoscan (mGµcm²)':lambda:0.001, #1mGycm2=0.001Gycm2
        'TECHNIX':lambda:0.01,#1µGym2=0.01Gycm2 
        'Technix (µGym²)':lambda:0.01,#1µGym2=0.01Gycm2 
        'ZIEHM SOLO':lambda:0.01, #1cGycm2=0.01Gycm2 
        'ZIEHM':lambda:0.01, #1cGycm2=0.01Gycm2 
        'Ziehm 8000 (cGycm²)':lambda:0.01,#1cGycm2=0.01Gycm2 
        'Artis Zee Floor 3 (µGym²)':lambda:0.01,#1µGym2=0.01Gycm2 
        'SOLO_FD':lambda:0.01,#1cGycm2=0.01Gycm2 
        'ARTIS':lambda:0.01,#1µGym2=0.01Gycm2 
        'ARTIS_BERL':lambda:0.01,#1µGym2=0.01Gycm2 
        '3-BERLIOZ':lambda:0.01,#1µGym2=0.01Gycm2 
        '2-STENDHAL':lambda:0.01,#1µGym2=0.01Gycm2 
        '1-CHAMPO':lambda:0.01,#1µGym2=0.01Gycm2 
        '1 - Champollion':lambda:1,#1µGym2=0.01Gycm2 'Siemens (µGym²) mais en hemolia donné en Gycm2 direct
        '2 - Stendhal':lambda:1,#1µGym2=0.01Gycm2 'Siemens (µGym²)
        '3 - Berlioz':lambda:1,#1µGym2=0.01Gycm2 'Siemens (µGym²)
        'Berlioz': lambda: 1,  # 1µGym2=0.01Gycm2 'Siemens (µGym²)
                }
    func=switcher.get(ampli,lambda:'Invalid')
    return func() 