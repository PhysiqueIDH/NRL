# %load_ext autoreload
# %autoreload 2
# %reload_ext autoreload


# import os
# dir="N:\\Themes\\Radioprotection GHM\\PYTHON_VSO\\NRLs\\spyder"
# # dir=r"C:\test_NRI\spyder"
# os.chdir(dir)
# # preparation de la base de données
# from preparation import preparation
# df=preparation()


#########################################" Faire ceci car la fusion de toutes les données a déjà été faite!
import os
import pandas as pd

dir="N:\\Themes\\Radioprotection GHM\\PYTHON_VSO\\NRLs\\spyder" 
# dir=r"C:\test_NRI\spyder" 
os.chdir(dir)
from fig_interactive import fig_int
from fig_interactive_ampli_med import fig_int_ampli_med
from fig_interactive_ampli_salle import fig_int_ampli_salle
from fig_interactive_interv import fig_int_int
# from fig_interactive_interv2 import fig_int_int2
# from fig_interactive_global import fig_int_int

from pie_nbtotal import pie_nb
# from pie_medecins import pie_nb
# import pie_medecins

dir=r"N:\Themes\Radioprotection GHM\PYTHON_VSO\NRLs\EXTRACTION" 
os.chdir(dir)
fil='ALL_BLOC_CICI_2014-2022_RX.xlsx'
sheet='Sheet1'
df= pd.read_excel (fil, sheet)
df=df.drop("Unnamed: 0",axis=1)
year=2021
ampli='CIOS'
interv='Cimentoplastie'


#doses all ampli
column='MOTIF_corr'
column='CATEGORY'
val='nbtotal'
val='moyenne Gycm2'
# stats=fig_int_int(df, year, column)
# stats=fig_int_int(df, year, interv)
stats=fig_int(df, year)

pie_nb(stats, year)
http://127.0.0.1:8050/


#doses 1 intervention
interv='Cimentoplastie'
interv='pose CCI'
interv='Picc line'
interv='Pacemaker simple'
interv='Pacemaker double'
year=[2014, 2020]
stats=fig_int_int(df, year, interv)


#medecins
stats_med=fig_int_ampli_med(df, year)
pie_nb(stats_med, year)

#je suis rest�e l�
stats_salle=fig_int_ampli_salle(df, year)
pie_nbtotal(stats_med, year)

#nb intervention total par sp�cialit�s et par ampli






# JE SUIS RESTEE LA: test_figure_interactive.py
# qui est l'environement d'essai de fig_interactive.py, connectee à plot_data
# il faut rajouter le choix du temps + moyenne, media, std... selon ce que lon choisi comme ampli/intervention
# après il faudra aussi corriger les donnees bizarres avec des explications

#### graphiques varies
# graphiques_varies.py voir!!
