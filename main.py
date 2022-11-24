# %load_ext autoreload
# %autoreload 2
# %reload_ext autoreload

# #
# import os
import os
import sys
dir="N:\\Themes\\Radioprotection GHM\\PYTHON_VSO\\NRLs\\Fork\\NRL"
# dir=r"C:\test_NRI\spyder"
os.chdir(dir)
# preparation de la base de données
from preparation import preparation
df=preparation()


#########################################" Faire ceci car la fusion de toutes les données a déjà été faite!
import os
import sys
dir="N:\\Themes\\Radioprotection GHM\\PYTHON_VSO\\NRLs\\Fork\\NRL"
# dir = "C:\\NRL\\Fork\\NRL"
os.chdir(dir)
import pandas as pd
from fig_interactive_GENERAL import fig_int_GENERAL
from fig_interactive_GENERAL_1param import fig_int_GENERAL_1param
from pie_GENERAL import pie_GENERALf
from pie_GENERAL_1param import pie_GENERAL_1paramf
from suivi_GENERAL import suivi_GENERAL
from boxplot_GENERAL import boxplot_GENERAL
# from fig_interactive_ampli_med import fig_int_ampli_med
# from fig_interactive_ampli_salle import fig_int_ampli_salle
# from fig_interactive_interv2 import fig_int_int2

#
# from pie_nbtotal import pie_nb
# from pie_medecins import pie_nb

# # #
dir=r"N:\Themes\Radioprotection GHM\PYTHON_VSO\NRLs\EXTRACTION"
# dir=r"C:\NRL\EXTRACTION"
os.chdir(dir)
fil='ALL_BLOC_CICI_2014-2022_RX.xlsx'
sheet='Sheet1'
df= pd.read_excel (fil, sheet)
df=df.drop("Unnamed: 0",axis=1)



# #doses all ampli
# column='MOTIF_corr'
# column='CATEGORY'
# year=2021
# stats=fig_int_int(df, year, column)
# stats=fig_int(df, year)

#
# # Plot interactive
param1='AMPLI'
param2='CATEGORY'
y1=2021
path_new = os.path.join(sys.path[0]+"\\results", param1+"-"+param2)
# path_new = os.path.join(sys.path[0]+"\\results", param1)
os.mkdir(path_new)
# for y1 in range(2021, 2022,1):
y2=y1
year=[y1, y2]
# # # calculate stats+interactive plots OK
stats=fig_int_GENERAL(df, year, param1, param2)
# stats=fig_int_GENERAL_1param(df, year, param1)
dir=sys.path[0]+"\\results\\"+param1
# y1=2021
# dir=sys.path[0]+"\\results\\"+param1+"-"+param2
os.chdir(dir)
# # read stats + pie plot
stats=pd.read_excel (str(y1)+'_stats.xlsx', 'Feuil1')
pie_GENERALf(stats)
# pie_GENERAL_1paramf(stats)
a
# http://127.0.0.1:8005/
# #
# param1 = 'AMPLI'
# param2 = 'CATEGORY'
# y1=2014
# y2=2021
# suivi_GENERAL([y1, y2], param1, param2)


# boxplot_GENERAL(df, [y1, y2], param1, param2)



# # #doses 1 intervention all this works!
# year=[2022, 2022]
# interv='Cimentoplastie'
# interv='pose CCI'
# interv='Picc line'
# interv='Pacemaker simple'
# interv='Pacemaker double'
# year=[2014, 2020]
# stats=fig_int_int(df, year, interv)




