# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 15:38:18 2018

@author: Anette
"""

import os
import csv
import pandas as pd
import numpy as np
# =============================================================================
# csv-tiedostonluku pandas-kirjastolla:
# =============================================================================


tiedostopolku = 'C:\\Users\\Anette\\python\\polttoainelaskuri\\'
csv_polku = os.path.join(tiedostopolku, 'autodata.csv')
#print(csv_polku)

#luetaan tiedosto, asetetaan 1. columni autonmerkiksi(muuten ei panda ymmarra)
#index_col = 'Auton merkki'
lue_csv = pd.read_csv(csv_polku)
#print(type(lue_csv))
#print(lue_csv)

#tehdään pandas dataframe, joka voidaan tallentaa csv-muotoon
uusi_lista = [['mersu', '70000', 5.6, 7.0 ],['maserati', '6800',12.2,9.7]]
uusi_tieto = np.array(uusi_lista)
#print(uusi_tieto)
uusi_data = pd.DataFrame(data = uusi_tieto, columns = ['automerkki', 'ajomaara', 'kulutettu polttoaine (litraa) kaupunki', 'polttoaineen kustannus (euroa) kaupunki'])
#print(uusi_data)
#Kirjoitetaan uusi csv-tiedosto
uusi_csv = 'C:\\Users\\Anette\\python\\polttoainelaskuri\\uusi_csvtiedosto.csv'
uusi_data.to_csv(uusi_csv)


lue = pd.read_csv(csv_polku)
print(lue[lue.columns[0]])

#lasketaan aiemmasta csv:stä tiedot uuteen tiedostoon
laske_csv = 'C:\\Users\\Anette\\python\\polttoainelaskuri\\autolaskuri.csv'
#print(laske_csv)



auto = np.array(lue[lue.columns[0]])
ajomaara = np.array([200,30000,100])
#lue[lue.columns[1]]*lue[lue.columns[2]]
kulutus = np.array(lue[lue.columns[1]]*ajomaara/100)
kustannus = np.array(lue[lue.columns[3]]*ajomaara/100)
#listana dataframelle sisäään ei toiminut, tuli rivit pystysarakkeiden sijaan
#datat = [[auto, ajomaara, kulutus, kustannus]]
#kokeillaan dictionarya, että saadaan datat sarakkeisiin (onnistui!)
datat = {'automerkki': auto,
         'ajomaara' : ajomaara, 
         'kulutettu polttoaine (litraa) kaupunki' : kulutus, 
         'polttoaineen kustannus (euroa) kaupunki' : kustannus}

#print(datat)
#tiedot = []

# =============================================================================
# #lisätään uudet tiedot dataframeen ja tallennetaan csv-muotoon
# =============================================================================
#uusi_tiedosto = pd.DataFrame(data = datat, columns =['automerkki', 'ajomaara', 'kulutettu polttoaine (litraa) kaupunki', 'polttoaineen kustannus (euroa) kaupunki'])
#koska käytetty dictionarua, ei tarvitse asettaa kolumneja enää
uusi_tiedosto = pd.DataFrame(data=datat)
#print(uusi_tiedosto)
#tallennetaan csv-muotooon
uusi_tiedosto.to_csv(laske_csv)

lue_laskuri = pd.read_csv(laske_csv)
print(lue_laskuri)


#%%
#avataan csv tiedosto
with open(csv_polku) as csv_tiedosto:
    csv_luku = csv.reader(csv_tiedosto, delimiter = ',')
    print(csv_luku)
    for rivi in csv_luku:
        print('csvllä %s' %rivi)
 
##tehdään uusi csv-tiedosto ja kirjoitetaan sinne       
#uusi_tiedosto = os.mkdir('C:\\Users\\Anette\\python\\polttoainelaskuri\\uusi_autotiedosto')        
#with open(uusi_tiedosto, 'w') as kirjoita_csv:
#    kirjoita = csv.writer(kirjoita_csv, delimiter = ',', )
#    
#    kirjoita.writerow(['mersu', 30.0, 5.6, 1.54])
#    
    

        
csv_tiedosto.close()
