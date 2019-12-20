# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 23:28:55 2018

@author: Anette
"""

import os
import cv2
import numpy as np
from scipy import ndimage

# dir_path = os.path.dirname(os.path.realpath(__file__))
# 
# print('current directory is %s' % dir_path)
# 
# #kansionpolku kuvaan
# kansionpolku = os.path.join(dir_path, 'Pictures', 'Kakka')


#kuvapolunalku = 'C:/Users/Anette/Pictures/'

#Polun määrittää käyttäjä syötteellä.
#kuvapolunloppusyotteesta = input('Anna kuvapolun kansionnimi: ')
#kuvapolku = os.path.join(kuvapolunalku, kuvapolunloppusyotteesta)

#kuvanpolku = kuvapolku + '/'
#print(kuvanpolku)


#%%        
class Kuva:
    
    def __init__(self, kuvannimet, kuvanpolku, kansionnimirot, kansionnimihar, kansiopienetkuvat):
        self.kuvannimet = kuvannimet
        self.kuvanpolku = kuvanpolku
        self.kansionnimirot = kansionnimirot
        self.kansionnimihar = kansionnimihar
        self.kansiopienetkuvat = kansiopienetkuvat
        
    
    def kuvanmuokkaus(self):
        
        for kuvannimi in self.kuvannimet:
#            kuvapolku = os.path.join(kuvanpolku, kuvannimi)
#            print(kuvapolku)
            #print(os.path.join(self.kuvanpolku, kuvannimi))
            kuva = cv2.imread(os.path.join(self.kuvanpolku, kuvannimi))
#            print(kuva.shape)
#            cv2.imshow('kuva', kuva)
#            cv2.waitKey(1)
            pienennettykuva = cv2.resize(kuva, (500, 500))
#           print(pienennettykuva.shape)
            pienet_polku = os.path.join(self.kansiopienetkuvat, 'pienet'+kuvannimi)
            print(pienet_polku)
            ret = cv2.imwrite(pienet_polku, pienennettykuva)
            print(ret)
            if np.random.random() < 0.3 :
                harmaasavy = cv2.cvtColor(pienennettykuva, cv2.COLOR_BGR2GRAY) 
#                print(harmaasavy)
                cv2.imwrite(os.path.join(self.kansionnimihar, 'harmaat'+kuvannimi), harmaasavy)   
            else:
                rotaatiokuva = ndimage.rotate(pienennettykuva, 45)
                cv2.imwrite(os.path.join(self.kansionnimirot, 'rotaatio'+kuvannimi), rotaatiokuva)
                
# 
 
#  
#%% Haetaan kansion sisällä olevat kansiot, ei kuvia tai muita tiedostoja !
kansiot = 'C:\\Users\\Anette\\Pictures\\pylly\\loppuvastus\\'
kansionnimet = [kansionnimi for kansionnimi in os.listdir(kansiot) if os.path.isdir(os.path.join(kansiot, kansionnimi))]

#for kansionnimi in os.listdir(kansiot):
#    if os.path.isdir(os.path.join(kansiot, kansionnimi)):
#        print(kansionnimi)

for kansionnimi in kansionnimet:
    kuvanpolku = os.path.join(kansiot, str(kansionnimi))
    uusi_kuvanpolku = kuvanpolku.replace('–', '_')
    uusi_kuvanpolku2 = uusi_kuvanpolku.replace(' ', '')
    os.rename(kuvanpolku, uusi_kuvanpolku2)  
    kuvanpolku = uusi_kuvanpolku2

    kuvannimet = [nimi for nimi in os.listdir(kuvanpolku) if nimi.endswith('.PNG') or nimi.endswith('.png') or nimi.endswith('.jpg')]
    #print(kuvannimet)

    
    kansionnimihar = os.path.join(kuvanpolku, 'harmaakuvat3\\')
    try:
        harmaakuvakansio = os.mkdir(kansionnimihar)
    except:
        print('Tiedosto harmaakuva on jo olemassa. Jatketaan.')
    
    kansionnimirot = os.path.join(kuvanpolku, 'rotaatiokuvat3\\')
    try:
        rotaatiokuvakansio = os.mkdir(kansionnimirot)
    except:
        print('Tiedosto rotaatiokuvat on jo olemassa. Jatketaan.')
        
    kansiopienetkuvat = os.path.join(kuvanpolku, 'pienetkuvat3\\')
    try:
        pienennetytkuvakansio = os.mkdir(kansiopienetkuvat)
    except:
        print('Tiedosto pienennetytkuvat on jo olemassa. Jatketaan.')
    print(kuvanpolku)
    print(kansionnimirot)
    print(kansionnimihar)
    print(kansiopienetkuvat)
    kansio = Kuva(kuvannimet, kuvanpolku, kansionnimirot, kansionnimihar, kansiopienetkuvat)
    kansio.kuvanmuokkaus()         