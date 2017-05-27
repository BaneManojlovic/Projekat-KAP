_author_='Tamara'

#Konzolna aplikacija za vizuelizaciju produktivnosti JPM
import sys
import os
import random
from klasa1 import *
from klasa2 import *
from klasa3 import *
from klasa4 import *

print("**************************************************************************")
print(" Dobrodosli u Python projekat: Vizuelizacija produktivnosti JPM")
print("**************************************************************************")
print(" Autor: student Tamara Lalic")
print("**************************************************************************")
print("\n")

#-------- Razne funkcije koje sam upotrebio -------------------------------
def funkcija_meni():
    print("*********** MENI ***********")
    print("Izaberite zeljenu opciju:")
    print("1. Prikaz analiziranog podrucja")
    print("2. Prikaz podataka iz baze")
    print("3. Produktivnost pojedinacne JPM po mesecima")
    print("4. Analiza zavisnosti izmedju varijabli")
    print("5. Analiza pomocu Linearne Regresije")
    print("6. Analiza pomocu Polinomijane Regresije")
    print("7. Izlaz iz programa")
    print("\n")
    return

def izbor_opcije():
    print("Odaberite zeljenu opciju:")
    opcija = sys.stdin.readline()
    return int(opcija)

#-------- MENI sekcija ----------------------------------------------
odgovor = 1
while (odgovor != 0):
    funkcija_meni()
    opcija = izbor_opcije()
    if (opcija == 1):
        print("1. Prikaz analiziranog podrucja")
        Klasa1().prikaz_slike()
        input('Press any key to continue . . . \n')
    elif (opcija == 2):
        print("2. Ispis podataka iz baze")
        Klasa1().prikaz_baze()
        input('Press any key to continue . . . \n')
    elif (opcija == 3):
        print("3. Produktivnost pojedinacne JPM po mesecima")
        Klasa1().produktivnost()
    elif (opcija == 4):
        print("4. Analiza zavisnosti izmedju varijabli")
        Klasa2().kljucne_varijable()
        input('Press any key to continue . . . \n')
        Klasa2().univarijantna_raspodela()
        input('\nPress any key to continue . . . \n')
    elif (opcija == 5):
        print("\n5. Analiza pomocu Linearne Regresije\n")
        Klasa3().linearna_regresija()
        input('Press any key to continue . . . \n')
        Klasa3().interval_poverenja()
        input('\nPress any key to continue . . . \n')
    elif (opcija == 6):
        print("\n6. Analiza pomocu Polinomijalne Regresije\n")
        Klasa4().polinomijalna()
        os.system('pause')
    elif (opcija == 7):
        print("\n******** Izasli ste iz programa - Dovidjenja! ****************************")
        print("**************************************************************************")
        sys.exit()
    else:
        print("Izabrali ste pogresan broj, pokusajte ponovo!")
        input('Press any key to continue . . . \n')
print("Kraj programa.")