# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 11:45:24 2021

@author: sorgato
"""


def salle_corrf(salle): 
    switcher={
        'S01': lambda:'Salle 1',
        'S02': lambda:'Salle 2',
        'S03': lambda:'Salle 3',
        'S04': lambda:'Salle 4',
        'S05': lambda:'Salle 5',
        'S06': lambda:'Salle 6',
        'S07': lambda:'Salle 7',
        'S08': lambda:'Salle 8',
        'S09': lambda:'Salle 9',
        'S10': lambda:'Salle 10',
        'S11': lambda:'Salle 11',
        'S12': lambda:'Salle 12',
        'S13': lambda:'Salle 13',
        'S14': lambda:'Salle 14',
        'Salle 1': lambda:'Salle 1',
        'Salle 2': lambda:'Salle 2',
        'Salle 3': lambda:'Salle 3',
        'Salle 4': lambda:'Salle 4',
        'Salle 5': lambda:'Salle 5',
        'Salle 6': lambda:'Salle 6',
        'Salle 7': lambda:'Salle 7',
        'Salle 8': lambda:'Salle 8',
        'Salle 9': lambda:'Salle 9',
        'Salle 10': lambda:'Salle 10',
        'Salle 11': lambda:'Salle 11',
        'Salle 12': lambda:'Salle 12',
        'Salle 13': lambda:'Salle 13',
        'Salle 14': lambda:'Salle 14',
        'ENDO1': lambda:'Endo 1',
        'ENDO2': lambda:'Endo 2',
        'ENDO3': lambda:'Endo 3',
        'ENDO4': lambda:'Endo 4',
        'Stendhal': lambda:'Stendhal',
        '2-STENDHAL': lambda:'Stendhal',
        '2 - Stendhal': lambda:'Stendhal',
        '1-CHAMPOLLION': lambda:'Champollion',
        '1 - Champollion': lambda:'Champollion',
        '3-BERLIOZ': lambda:'Berlioz',
        '3 - Berlioz': lambda:'Berlioz',
        'Berlioz': lambda:'Berlioz',
        '4-SSPICICI': lambda:'CICI'
                }
    func=switcher.get(salle,lambda:'Invalid')
    return func() 