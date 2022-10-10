# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 19:08:43 2021

@author: sorgato
"""

#  com=['imento']
   #  replace=['Cimentoplastie']
   #  types_corr=clean_typesf(com, replace, types_corr)
   #  types_corr=np.unique(types_corr)
     
   #  com=['vert']
   #  replace=['Cimentoplastie']
   #  types_corr=clean_typesf(com, replace, types_corr)
   #  types_corr=np.unique(types_corr)

   #  com=['Vert']
   #  replace=['Cimentoplastie']
   #  types_corr=clean_typesf(com, replace, types_corr)
   #  types_corr=np.unique(types_corr)    

   #  com=['oelio']
   #  replace=['Cholecystectomie']
   #  types_corr=clean_typesf(com, replace, types_corr)
   #  types_corr=np.unique(types_corr)

   #  com=['holécystect']
   #  replace=['Cholecystectomie']
   #  types_corr=clean_typesf(com, replace, types_corr)
   #  types_corr=np.unique(types_corr)
    
   #  com=['rthrod'] 
   #  replace=['Ostéosynthèse/Arthrodèse'] #ouvert
   #  types_corr=clean_typesf(com, replace, types_corr)
   #  types_corr=np.unique(types_corr)
    
   #  com=['rthorod'] 
   #  replace=['Ostéosynthèse/Arthrodèse'] #ouvert
   #  types_corr=clean_typesf(com, replace, types_corr)
   #  types_corr=np.unique(types_corr)
    
   #  com=['Dynesys'] 
   #  replace=['Ostéosynthèse/Arthrodèse'] #ouvert
   #  types_corr=clean_typesf(com, replace, types_corr)
   #  types_corr=np.unique(types_corr)
    
   #  com=['Colonne ostéosynthèse']#ouvert (pas percutanée) arthrodèse
   #  replace=['Ostéosynthèse/Arthrodèse'] #ouvert
   #  types_corr=clean_typesf(com, replace, types_corr)
   #  types_corr=np.unique(types_corr)  
    
   #  com=['osteosynthèse percut']#pas ouvert
   #  replace=['Osteosynthèse Percutanée']
   #  types_corr=clean_typesf(com, replace, types_corr)  
   #  types_corr=np.unique(types_corr)   
    
   #  com=['ostéosynthese percut']#pas ouvert
   #  replace=['Osteosynthèse Percutanée']
   #  types_corr=clean_typesf(com, replace, types_corr)  
   #  types_corr=np.unique(types_corr)  
    
   #  com=['ostéosynthèse percut']#pas ouvert
   #  replace=['Osteosynthèse Percutanée']
   #  types_corr=clean_typesf(com, replace, types_corr)  
   #  types_corr=np.unique(types_corr)   
    
   #  com=['rhisolyse'] #+luxation #manipulation pour mettre en place
   #  replace=['Colonne rhisolyse']
   #  types_corr=clean_typesf(com, replace, types_corr)
   #  types_corr=np.unique(types_corr)

   #  com=['Colonne lavage']#ouvert (pas percutanée) arthrodèse
   #  replace=['Colonne lavage cicatrice']
   #  types_corr=clean_typesf(com, replace, types_corr)
   #  types_corr=np.unique(types_corr) 
   
   
   #  com=['onde JJ']
   #  replace=['Uretéroscopie']
   #  types_corr=clean_typesf(com, replace, types_corr)
   #  types_corr=np.unique(types_corr)


   #  com=['re changement de sonde']
   #  replace=['Uretéroscopie']
   #  types_corr=clean_typesf(com, replace, types_corr)
   #  types_corr=np.unique(types_corr)
    
   #  com=['rétéroscopie']
   #  replace=['Uretéroscopie']
   #  types_corr=clean_typesf(com, replace, types_corr)
   #  types_corr=np.unique(types_corr)
    
 
   #  com=['reterectomie'] #+nephro ureterectomie
   #  replace=['Uretérèctomie']
   #  types_corr=clean_typesf(com, replace, types_corr)
   #  types_corr=np.unique(types_corr)
    
   #  com=['endo']
   #  replace=['Endoscopie']
   #  types_corr=clean_typesf(com, replace, types_corr)    
   #  types_corr=np.unique(types_corr)
 
   #  com=['astro']
   #  replace=['Endoscopie']
   #  types_corr=clean_typesf(com, replace, types_corr)    
   #  types_corr=np.unique(types_corr)
 
   #  com=['rothèse colique']#endoscopie +proth duodénale oesaphagienne
   #  replace=['Endoscopie']
   #  types_corr=clean_typesf(com, replace, types_corr)    
   #  types_corr=np.unique(types_corr)

   #  com=['rothèse duodénale']#endoscopie +proth duodénale oesaphagienne
   #  replace=['Endoscopie']
   #  types_corr=clean_typesf(com, replace, types_corr)    
   #  types_corr=np.unique(types_corr)
    
   #  com=['rothèse oesophagi']#endoscopie +proth duodénale oesaphagienne
   #  replace=['Endoscopie']
   #  types_corr=clean_typesf(com, replace, types_corr)    
   #  types_corr=np.unique(types_corr)
    
   #  com=['athétérisme'] #cathétérisme
   #  replace=['Douleur']
   #  types_corr=clean_typesf(com, replace, types_corr)
   #  types_corr=np.unique(types_corr)
    
   #  com=['eurostim'] #neurostimulation
   #  replace=['Douleur']
   #  types_corr=clean_typesf(com, replace, types_corr)
   #  types_corr=np.unique(types_corr)

   #  com=['pompe'] #ablation pompe
   #  replace=['Douleur']
   #  types_corr=clean_typesf(com, replace, types_corr)
   #  types_corr=np.unique(types_corr)
    
   #  com=['euro'] #ablation pompe
   #  replace=['Douleur']
   #  types_corr=clean_typesf(com, replace, types_corr)
   #  types_corr=np.unique(types_corr)
    
    
   #  com=['POSE DE CHAMBRE'] #pose port a cath
   #  replace=['PAC']
   #  types_corr=clean_typesf(com, replace, types_corr)
   #  types_corr=np.unique(types_corr)
    
   #  com=['ose port'] #pose port a cath
   #  replace=['PAC']
   #  types_corr=clean_typesf(com, replace, types_corr)
   #  types_corr=np.unique(types_corr)
    
   #  com=['PAC'] #pose port a cath
   #  replace=['PAC']
   #  types_corr=clean_typesf(com, replace, types_corr)
   #  types_corr=np.unique(types_corr)
    
   #  com=['aminectomie'] #herniectomie + corporectomie+ostéotomie
   #  replace=['Laminectomie/Herniectomie/Ostéotomie']
   #  types_corr=clean_typesf(com, replace, types_corr)
   #  types_corr=np.unique(types_corr)

   #  com=['erniectomie'] #herniectomie + corporectomie+ostéotomie
   #  replace=['Laminectomie/Herniectomie/Ostéotomie']
   #  types_corr=clean_typesf(com, replace, types_corr)
   #  types_corr=np.unique(types_corr)        

   #  com=['orporectomie'] #herniectomie + corporectomie+ostéotomie
   #  replace=['Laminectomie/Herniectomie/Ostéotomie']
   #  types_corr=clean_typesf(com, replace, types_corr)
   #  types_corr=np.unique(types_corr)

   #  com=['Colonne ostéotomie'] #herniectomie + corporectomie+ostéotomie
   #  replace=['Laminectomie/Herniectomie/Ostéotomie']
   #  types_corr=clean_typesf(com, replace, types_corr)
   #  types_corr=np.unique(types_corr)
    
   #  com=['olonne ablation'] #'repose depose materiel
   #  replace=['Colonne ablation matériel']
   #  types_corr=clean_typesf(com, replace, types_corr)
   #  types_corr=np.unique(types_corr)
       
   #  # com=['rhisolyse'] 
   #  # replace=['?']

   #  com=['hrombectomie'] #désobstruction
   #  replace=['Thrombectomie']
   #  types_corr=clean_typesf(com, replace, types_corr)
   #  types_corr=np.unique(types_corr)
    
   #  com=['sobstruction'] #désobstruction
   #  replace=['Thrombectomie']
   #  types_corr=clean_typesf(com, replace, types_corr)
   #  types_corr=np.unique(types_corr)
    
   #  com=['Endartériectomie'] #désobstruction
   #  replace=['Thrombectomie']
   #  types_corr=clean_typesf(com, replace, types_corr)
   #  types_corr=np.unique(types_corr)
     
   #  com=['nfiltration'] #injection antiinflammatoire/corticoide dans rachis/scarum, rapide!
   #  replace=['Infiltration']
   #  types_corr=clean_typesf(com, replace, types_corr)
   #  types_corr=np.unique(types_corr)
  
   # #Bras synthèse 
   #  com=['Bras synt'] #
   #  replace=['Synthèse Bras']
   #  types_corr=clean_typesf(com, replace, types_corr)
   #  types_corr=np.unique(types_corr)
    
   #  com=['umérus synt'] #
   #  replace=['Synthèse Bras']
   #  types_corr=clean_typesf(com, replace, types_corr)
   #  types_corr=np.unique(types_corr)
    
   #  #Cheville synthèse 
   #  com=['Cheville synt']
   #  replace=['Synthèse Cheville']
   #  types_corr=clean_typesf(com, replace, types_corr)
   #  types_corr=np.unique(types_corr)

   #  com=['Cheville greffe']
   #  replace=['Synthèse Cheville']
   #  types_corr=clean_typesf(com, replace, types_corr)
   #  types_corr=np.unique(types_corr)

   #  com=['bimallé'] 
   #  replace=['Synthèse Cheville']
   #  types_corr=clean_typesf(com, replace, types_corr)
   #  types_corr=np.unique(types_corr)
    
   #  com=['éduction'] #+luxation #manipulation pour mettre en place
   #  replace=['Réduction']
   #  types_corr=clean_typesf(com, replace, types_corr)
   #  types_corr=np.unique(types_corr)
    
   #  com=['eduction'] #+luxation #manipulation pour mettre en place
   #  replace=['Réduction']
   #  types_corr=clean_typesf(com, replace, types_corr)
   #  types_corr=np.unique(types_corr)
    
   #  com=['luxation'] #+luxation #manipulation pour mettre en place
   #  replace=['Réduction']
   #  types_corr=clean_typesf(com, replace, types_corr)
   #  types_corr=np.unique(types_corr)

   #  com=['LUXATION'] #+luxation #manipulation pour mettre en place
   #  replace=['Réduction']
   #  types_corr=clean_typesf(com, replace, types_corr)
   #  types_corr=np.unique(types_corr)
    
   #  com=['Epaule synthèse'] # PTE 
   #  replace=['Synthèse Epaule']
   #  types_corr=clean_typesf(com, replace, types_corr)  
   #  types_corr=np.unique(types_corr)

   #  com=['Epaule PTE'] #
   #  replace=['Synthèse Epaule']
   #  types_corr=clean_typesf(com, replace, types_corr)  
   #  types_corr=np.unique(types_corr)


   #  com=['Femur synthèse'] #hanche fémur DHS + jambe synthèse
   #  replace=['Synthèse Femur']
   #  types_corr=clean_typesf(com, replace, types_corr)  
   #  types_corr=np.unique(types_corr)
    
   #  com=['ambe synth'] # jambe synthèse
   #  replace=['Synthèse Femur']
   #  types_corr=clean_typesf(com, replace, types_corr)  
   #  types_corr=np.unique(types_corr)   
       
   #  com=['fémur DHS'] #hanche fémur DHS + jambe synthèse
   #  replace=['Synthèse Femur']
   #  types_corr=clean_typesf(com, replace, types_corr)  
   #  types_corr=np.unique(types_corr)

   #  com=['Hanche arthrosco'] #hanche fémur DHS + jambe synthèse
   #  replace=['Arthroscopie Hanche']
   #  types_corr=clean_typesf(com, replace, types_corr)  
   #  types_corr=np.unique(types_corr)
       

   #  com=['fémur clou'] #hanche fémur DHS + jambe synthèse
   #  replace=['Clou Femur']
   #  types_corr=clean_typesf(com, replace, types_corr)  
   #  types_corr=np.unique(types_corr)
 
   #  # com=['clou'] #hanche fémur DHS + jambe synthèse
   #  # replace=['Clou Femur']
   #  # types_corr=clean_typesf(com, replace, types_corr)  
   #  # types_corr=np.unique(types_corr)
    
   #  com=['enou synth'] #genou otv genou synthèse plateua tibial
   #  replace=['Synthèse Genou']
   #  types_corr=clean_typesf(com, replace, types_corr)  
   #  types_corr=np.unique(types_corr)
    
   #  com=['enou OTV'] #genou otv genou synthèse plateua tibial
   #  replace=['Synthèse Genou']
   #  types_corr=clean_typesf(com, replace, types_corr)  
   #  types_corr=np.unique(types_corr)    
    
 
   #  com=['urage'] #+luxation #manipulation pour mettre en place
   #  replace=['Curage axillaire']
   #  types_corr=clean_typesf(com, replace, types_corr)
   #  types_corr=np.unique(types_corr)

   #  com=['ied hallux'] #
   #  replace=['Pied hallux valgus']
   #  types_corr=clean_typesf(com, replace, types_corr) 
   #  types_corr=np.unique(types_corr)
     
   #  com=['Kt'] #+luxation #manipulation pour mettre en place
   #  replace=['Kt']
   #  types_corr=clean_typesf(com, replace, types_corr)
   #  types_corr=np.unique(types_corr)

   #  com=['ontage'] #
   #  replace=['Pontage']
   #  types_corr=clean_typesf(com, replace, types_corr)
   #  types_corr=np.unique(types_corr)

   #  com=['ein mastectomie'] #
   #  replace=['Mastectomie']
   #  types_corr=clean_typesf(com, replace, types_corr)
   #  types_corr=np.unique(types_corr)


   #  com=['laparotomie'] #recherche compresse/problème
   #  replace=['Laparotomie']
   #  types_corr=clean_typesf(com, replace, types_corr)
   #  types_corr=np.unique(types_corr)
    

   #  com=['ablation broche'] 
   #  replace=['?']
   #  types_corr=clean_typesf(com, replace, types_corr)
