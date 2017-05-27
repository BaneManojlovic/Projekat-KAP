_author_='Tamara'

import sys
import os
import csv
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from numpy import *
from scipy.interpolate import *

class Klasa4:
#--------------- Funcije za opciju 6 ---------------------------------------------------------------------------------
    def polinomijalna(self):
        print('Regresije')
        baza = pd.read_csv("baza.csv")
        baza.columns = ['Organizaciona celina', 'Januar', 'Februar', 'Mart', 'April',  'Maj', 'Jun', 'Jul', 'Avgust',
                        'Septembar', 'Oktobar', 'Novembar', 'Prosecna produktivnost','Stalno aktivni salteri',
                        'Povremeno aktivni salteri', 'Neaktivni salteri', 'Ukupno saltera u posti',
                        'Automatizovani salteri', 'Univerzalni salteri', 'Salteri uplata isplata']
        X = baza['Ukupno saltera u posti'].values
        Y = baza['Prosecna produktivnost'].values
#----------- Izracunavanje koeficijenata za LR -----------------------------------------------
        print('\na. Linearna regresija')
        pl = polyfit(X, Y, 1)
        print('Koeficijenti PL su:')
        print(pl)
        print('Regresiona jednacina za LR: ')
        print('\t Y = %.3f'  % pl[1],'+ %.3f'  % pl[0], '* X' )
#------------ Prikaz produktivnosti ----------------------------------------------------------
        plt.title('Prikaz ostvarene produktivnosti JPM')
        plt.xlabel('Ukupno saltera u posti')
        plt.ylabel('Produktivnost')
        plt.plot(X, Y, 'o')
        plt.show()
        os.system('pause')
#------------ Linearna regresija -------------------------------------------------------------
        plt.title('Prikaz ostvarene produktivnosti i regresione prave (LR)')
        plt.xlabel('Ukupno saltera u posti')
        plt.ylabel('Produktivnost')
        plt.plot(X,Y, 'o')
        plt.plot(X, polyval(pl, X), 'r-')
        plt.show()
        os.system('pause')
#----------- Izracunavanje koeficijenata za PR -----------------------------------------------
        print('\nb. Polinomijalna regresija')
        p2 = polyfit(X, Y, 2)
        print('Koeficijenti PR su:')
        print(p2)
        print('Regresiona jednacina za PR: ')
        print('\t Y = %.3f'  % p2[1],'+ %.3f'  % p2[0], '* X' )
#----------- Polinomijalna regresija ---------------------------------------------------------
        plt.title('Prikaz ostvarene produktivnosti i regresione prave (PR)')
        plt.xlabel('Ukupno saltera u posti')
        plt.ylabel('Produktivnost')
        plt.plot(X,Y, 'o')
        plt.plot(X, polyval(pl, X), 'r-')
        plt.plot(X, polyval(p2, X), 'g--')
        plt.show()