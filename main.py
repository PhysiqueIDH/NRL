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
# dir="N:\\Themes\\Radioprotection GHM\\PYTHON_VSO\\NRLs\\Pycharm"
dir = r"C:\NRL\Fork\NRL"
os.chdir(dir)
import pandas as pd
# from pie_GENERAL import pie_GENERALf as pie_GENERALf

# from fig_interactive_GENERAL import fig_int_GENERAL as fig_int_GENERAL
# from fig_interactive_ampli_med import fig_int_ampli_med
# from fig_interactive_ampli_salle import fig_int_ampli_salle
# from fig_interactive_interv2 import fig_int_int2
# from fig_interactive_global import fig_int_int
#
# from pie_nbtotal import pie_nb
# from pie_medecins import pie_nb


# dir=r"N:\Themes\Radioprotection GHM\PYTHON_VSO\NRLs\EXTRACTION"
# dir=r"C:\NRL\EXTRACTION"
# os.chdir(dir)
# fil='ALL_BLOC_CICI_2014-2022_RX.xlsx'
# sheet='Sheet1'
# df= pd.read_excel (fil, sheet)
# df=df.drop("Unnamed: 0",axis=1)



# #doses all ampli
# # column='MOTIF_corr'
# column='CATEGORY'
# # val='nbtotal'
# # val='moyenne Gycm2'
# # stats=fig_int_int(df, year, interv)
# stats=fig_int(df, year)


# Plot interactive
# year=[2022, 2022]
# param1='AMPLI'
# param2='NOMPRATICIEN'
dir=r"C:\NRL\Fork\results"
os.chdir(dir)

# # # calculate stats+interactive plots OK
# stats=fig_int_GENERAL(df, year, param1, param2)
# # stats.to_excel('stats.xlsx', sheet_name='Feuil1')

# read stats + pie plot
stats=pd.read_excel ('stats.xlsx', 'Feuil1')
pie_GENERALf(stats)
# http://127.0.0.1:8005/
# #
#
# # #doses 1 intervention all this works!
# year=[2022, 2022]
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
# pie_nb(stats, 2022, column)
# http://127.0.0.1:8050/
#



