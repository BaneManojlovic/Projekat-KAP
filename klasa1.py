_author_='Tamara'

import PIL
import sys
import os
import matplotlib.pyplot as plt
from PIL import Image
import csv
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats
import io

class Klasa1:
#----------- Funkcije za opciju 1. ------------------------------------------------------------------------------------
    def prikaz_slike(self):
        print(" \na. Prostorni prikaz analiziranog podrucja")
        image = Image.open('slika01.jpg')
        image.show()
        input('Press any key to continue . . . ')
        print(" b. Prikaz rasporeda jedinica postanske mreze")
        image = Image.open('slika02.jpg')
        image.show()

#----------- Funkcije za opciju 2. ------------------------------------------------------------------------------------
    def prikaz_baze(self):
        # 1.Korak - Ucitavam podatke iz fajla
        baza = pd.read_csv("baza.csv")
        baza.columns = ['Organizaciona celina', 'Januar', 'Februar', 'Mart', 'April',  'Maj', 'Jun', 'Jul', 'Avgust',
                        'Septembar', 'Oktobar', 'Novembar', 'Prosecna produktivnost','Stalno aktivni salteri',
                        'Povremeno aktivni salteri', 'Neaktivni salteri', 'Ukupno saltera u posti',
                        'Automatizovani salteri', 'Univerzalni salteri', 'Salteri uplata isplata']
        print('\na. Primer ispisa dela podataka iz baze:\n')
        print(baza.head(5))
        input('Press any key to continue . . . ')
        print('\nb. Opis podataka iz baze:')
        print('(Broj Organizacionih celina, Broj obelezja) = ', baza.shape)
        input('\nPress any key to continue . . . ')
        print('\nc. Detaljan opis podataka:')
        print(baza.describe())

    def produktivnost(self):
        baza = pd.read_csv("baza.csv")
        baza.columns = ['Organizaciona celina', 'Januar', 'Februar', 'Mart', 'April',  'Maj', 'Jun', 'Jul', 'Avgust',
                        'Septembar', 'Oktobar', 'Novembar', 'Prosecna produktivnost','Stalno aktivni salteri',
                        'Povremeno aktivni salteri', 'Neaktivni salteri', 'Ukupno saltera u posti',
                        'Automatizovani salteri', 'Univerzalni salteri', 'Salteri uplata isplata']

        print("\nOdaberite zeljenu JPM (unesite redni broj):")
        with open('baza.csv','r') as longishfile:
            reader=csv.reader(longishfile)
            rows=[r for r in reader]
            jpm = sys.stdin.readline()
            jpm = int(jpm)
            print("\na. Parametri JPM: ")
          #  print (rows[jpm])           #Ispisuje liniju sa parametrima JPM
            vrednosti = rows[jpm]
            print('\tOrganizaciona jedinica: ', vrednosti[0])
            print('\tStalno aktivnih saltera: ',vrednosti[13])
            print('\tPovremeno aktivnih saltera: ', vrednosti[14])
            print('\tNeaktivnih saltera: ', vrednosti[15])
            print('\tAutomatizovanih saltera: ', vrednosti[17])
            print('\tUniverzalnih saltera: ', vrednosti[18])
            print('\tSaltera uplata/isplata: ', vrednosti[19])
            print('\tUkupno saltera u JPM: ', vrednosti[16] ,'\n')
            os.system('pause')

            print('b. Graficki prikaz produktivnosti JPM broj: ', vrednosti[0])
            T = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
            K = np.array([float(vrednosti[1]),float(vrednosti[2]),float(vrednosti[3]),float(vrednosti[4]),
                           float(vrednosti[5]),float(vrednosti[6]),float(vrednosti[7]),float(vrednosti[8]),
                      float(vrednosti[9]),float(vrednosti[10]),float(vrednosti[11])])
            my_xticks = ['Januar','Februar','Mart','April', 'Maj', 'Jun', 'Jul', 'Avgust', 'Septembar', 'Oktobar', 'Novembar']
            plt.ylabel('Produktivnost')
            plt.title('Produktivnost odabrane JPM')
            plt.grid(True)
            plt.xticks(T, my_xticks, rotation='45')
            plt.plot(T, K, 'b-')
            plt.show()
            os.system('pause')