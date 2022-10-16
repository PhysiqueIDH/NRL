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

# dir="N:\\Themes\\Radioprotection GHM\\PYTHON_VSO\\NRLs\\Pycharm"
dir=r"C:\NRL\Fork\NRL"
os.chdir(dir)
from fig_interactive_GENERAL import fig_int_GENERAL as fig_int_GENERAL
# from fig_interactive_ampli_med import fig_int_ampli_med
# from fig_interactive_ampli_salle import fig_int_ampli_salle
# from fig_interactive_interv2 import fig_int_int2
# from fig_interactive_global import fig_int_int
#
# from pie_nbtotal import pie_nb
# from pie_medecins import pie_nb
from pie_GENERAL import pie_GENERAL

# dir=r"N:\Themes\Radioprotection GHM\PYTHON_VSO\NRLs\EXTRACTION"
dir=r"C:\NRL\EXTRACTION"
os.chdir(dir)
fil='ALL_BLOC_CICI_2014-2022_RX.xlsx'
sheet='Sheet1'
df= pd.read_excel (fil, sheet)
df=df.drop("Unnamed: 0",axis=1)
# year=2021
# ampli='CIOS'
# interv='Cimentoplastie'


# #doses all ampli
# # column='MOTIF_corr'
# # column='CATEGORY'
# # val='nbtotal'
# # val='moyenne Gycm2'
# # stats=fig_int_int(df, year, interv)
# stats=fig_int(df, year)



year=[2022, 2022]
# stats=fig_int_GENERAL(df, year, 'AMPLI', 'CATEGORY')
# stats=fig_int_GENERAL(df, year, 'SALLE', 'AMPLI')
# stats=fig_int_GENERAL(df, year, 'NOMPRATICIEN', 'CATEGORY')
# stats=fig_int_GENERAL(df, year, 'NOMPRATICIEN', 'AMPLI')
stats=fig_int_GENERAL(df, year, 'AMPLI', 'NOMPRATICIEN')
#
pie_GENERAL(stats, year,'AMPLI', 'NOMPRATICIEN')
# http://127.0.0.1:8050/
#
#
# # #doses 1 intervention
# interv='Cimentoplastie'
# interv='pose CCI'
# interv='Picc line'
# interv='Pacemaker simple'
# interv='Pacemaker double'
# year=[2014, 2020]
# stats=fig_int_int(df, year, interv)
# #
#
# #medecins
# stats_med=fig_int_ampli_med(df, year)
# pie_nb(stats_med, year)
#
# #je suis rest�e l�
# stats_salle=fig_int_ampli_salle(df, year)
# pie_nbtotal(stats_med, year)
#
# #nb intervention total par sp�cialit�s et par ampli
#
#
#
#
#
#
# # JE SUIS RESTEE LA: test_figure_interactive.py
# # qui est l'environement d'essai de fig_interactive.py, connectee à plot_data
# # il faut rajouter le choix du temps + moyenne, media, std... selon ce que lon choisi comme ampli/intervention
# # après il faudra aussi corriger les donnees bizarres avec des explications
#
# #### graphiques varies
# # graphiques_varies.py voir!!
