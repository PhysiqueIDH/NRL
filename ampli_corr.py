# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 11:45:24 2021

@author: sorgato
"""


def ampli_corrf(ampli): 
    # import pandas as pd
    # ampli=pd.Series(ampli)  
    switcher={
        # '21    SIEM_CIOS\nName: AMPLI, dtype: object': lambda:1,#µGym2
        'SIEM_CIOS': lambda:'CIOS',#µGym2            'Siemens (µGym²)':lambda:1,#µGym2
        'CIOS Fusion (µGym²)':lambda:'CIOS',#µGym2
        'Siemens (µGym²)':lambda:'CIOS',#µGym2
        'SIEM_VARIC':lambda:'VARIC',#1cGycm2=1µGym2
        'Siemens Varic (cGycm²)':lambda:'VARIC',#1cGycm2=1µGym2
        'ORTHOSCAN':lambda:'ORTHOSCAN', #1mGycm2=0.1µGym2
        'Orthoscan (mGµcm²)':lambda:'ORTHOSCAN', #1mGycm2=0.1µGym2
        'TECHNIX':lambda:'TECHNIX', #µGym2
        'Technix (µGym²)':lambda:'TECHNIX', #µGym2
        'ZIEHM':lambda:'ZIEHM', #1cGycm2=1µGym2
        'Ziehm 8000 (cGycm²)':lambda:'ZIEHM', #1cGycm2=1µGym2   
        'ZIEHM SOLO':lambda:'ZIEHM SOLO', #1cGycm2=1µGym2 
        'SOLO_FD':lambda:'ZIEHM SOLO', #µGym2
        'Artis Zee Floor 3 (µGym²)': lambda:'ARTIS',#µGym2
        '4-SSPICICI': lambda:'ARTIS',#µGym2
        '1 - Champollion': lambda:'Champollion',
        '1-CHAMPOLLION': lambda:'Champollion',
        '2 - Stendhal': lambda:'Stendhal',
        '3-STENDHAL': lambda:'Stendhal',
        '3 - Berlioz': lambda:'Berlioz',
        '3-BERLIOZ': lambda:'Berlioz',
        'ENDO1': lambda:'Endoscopie',
        'ENDO2': lambda:'Endoscopie',
        'ENDO3': lambda:'Endoscopie',
        'ENDO4': lambda:'Endoscopie',
                }
    func=switcher.get(ampli,lambda:'Invalid')
    return func() 