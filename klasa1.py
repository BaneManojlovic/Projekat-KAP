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
        print('\nPrimer ispisa dela podataka iz baze:\n')
        print(baza.head(5))
        input('Press any key to continue . . . ')
        print('\na. Opis podataka iz baze:')
        print('(Broj Organizacionih celina, Broj obelezja) = ', baza.shape)
        input('\nPress any key to continue . . . ')
        print('\nb. Detaljan opis podataka:')
        print(baza.describe())



    def produktivnost(self):
        baza = pd.read_csv("baza.csv")
        baza.columns = ['Organizaciona celina', 'Januar', 'Februar', 'Mart', 'April',  'Maj', 'Jun', 'Jul', 'Avgust',
                        'Septembar', 'Oktobar', 'Novembar', 'Prosecna produktivnost','Stalno aktivni salteri',
                        'Povremeno aktivni salteri', 'Neaktivni salteri', 'Ukupno saltera u posti',
                        'Automatizovani salteri', 'Univerzalni salteri', 'Salteri uplata isplata']
    #11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        #data = [['a','b'], ['a','c'], ['b','d']]
        M = baza.head(20)    #<--- Uzimam samo prvih 20 redova iz baze za ilustraciju
        search = M['Organizaciona celina'].values
        print("Odaberite zeljenu JPM:")
        jpm = sys.stdin.readline()

   #     data = [['a','b'], ['a','c'], ['b','d']]
     #   search = 'c'
      #  any(e[1] == jpm for e in search)
        result = [element for element in search if element[1] == jpm]
        print(result)

     #   search = 'c'
     #   for sublist in search:
     #       if sublist[1] == jpm:
     #           print( "Found it!", sublist)
     #       break

    #1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
 #       M = baza.head(20)    #<--- Uzimam samo prvih 20 redova iz baze za ilustraciju
 #       A = M['Organizaciona celina'].values
 #       B = M['Domacinstva'].values
 #       C = M['Pravna lica'].values
 #       D = M['Korisnici'].values

 #       print(" d. Graficki prikaz broja analiziranih domacinstava")
 #       plt.title('Prikaz broja domacinstava na svakom PAK-u (parcijalni uzorak)')
 #       width = 1/1.5
 #       plt.bar(A, B, width, color="blue")
 #       plt.xlabel('PAK')
 #       plt.ylabel('Domacinstva')
 #       plt.grid(True)
 #       plt.show()
        """
        input('Press any key to continue . . . ')
        print(" e. Graficki prikaz broja analiziranih pravnih lica ")
        plt.title('Prikaz broja registrovanih pravnih lica na svakom PAK-u (parcijalni uzorak)')
        width = 1/1.5
        plt.bar(A, C, width, color="red")
        plt.xlabel('PAK')
        plt.ylabel('Pravna lica')
        plt.grid(True)
        plt.show()

        input('Press any key to continue ...')
        print(" f. Graficki prikaz ukupnog broja analiziranih svih korisnika zajedno ")
        plt.title('Prikaz broja svih korisnika na svakom PAK-u (parcijalni uzorak)')
        width = 1/1.5
        plt.bar(A, D, width, color="green")
        plt.xlabel('PAK')
        plt.ylabel('Korisnici')
        plt.grid(True)
        plt.show()
        """

    """
    def kategorije(self):
        print('c. Prikaz posiljaka prema tipovima ')
        baza = pd.read_csv("baza.csv")
        baza.columns = ['PAK', 'Objekti', 'Broj spratova', 'Domacinstva', 'Pravna lica stan',  'Pravna lica lokal',
                        'Pravna lica', 'Korisnici', 'Liftovi', 'Sanducici', 'O', 'OS', 'R' ,'RS', 'AR', 'ARS', 'PU',
                        'TR10', 'V', 'Votk', 'Ropt', 'Rino', 'TG', 'Posiljke']
        labels = 'O', 'OS', 'R' ,'RS', 'AR', 'ARS', 'PU', 'TR10', 'V', 'Votk', 'Ropt', 'Rino', 'TG'
        sizes = [max(baza[['O']].values), max(baza[['OS']].values), max(baza[['R']].values), max(baza[['RS']].values),
                 max(baza[['AR']].values), max(baza[['ARS']].values), max(baza[['PU']].values), max(baza[['TR10']].values),
                 max(baza[['V']].values), max(baza[['Votk']].values), max(baza[['Ropt']].values), max(baza[['Rino']].values),
                 max(baza[['TG']].values)]
        plt.pie(sizes,  labels=labels, autopct='%1.1f%%', startangle=55)
        plt.title('Broj posiljaka po tipovima\n')
        plt.axis('equal')
        plt.show()
    """