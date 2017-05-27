_author_='Tamara'

import sys
import os
import csv
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
import math
from random import randint

class Klasa3:
#------------- Funkcije za opciju 5 -----------------------------------------------------------------------------------
    def linearna_regresija(self):
        # 1.Korak - Ucitavam podatke iz fajla
        baza = pd.read_csv("baza.csv")
        baza.columns = ['Organizaciona celina', 'Januar', 'Februar', 'Mart', 'April',  'Maj', 'Jun', 'Jul', 'Avgust',
                        'Septembar', 'Oktobar', 'Novembar', 'Prosecna produktivnost','Stalno aktivni salteri',
                        'Povremeno aktivni salteri', 'Neaktivni salteri', 'Ukupno saltera u posti',
                        'Automatizovani salteri', 'Univerzalni salteri', 'Salteri uplata isplata']
        print('\na. Analiza podataka pomocu Linearne regresije ')
        X = baza[['Ukupno saltera u posti']].values
        Y = baza['Prosecna produktivnost'].values
        slr = LinearRegression()
        slr.fit(X, Y)    # Fit regression model
        print('\nKoeficijenti:')
        print(' b1 = %.3f ' % slr.coef_[0], ', (slope)')              # Koeficijent b1 (beta1)
        print(' b0 = %.3f' % slr.intercept_, ', (intercept)')         # Koeficijent bo (beta0)
        print('\nRegresiona jednacina:')
        print('\t Y = %.3f'  % slr.intercept_,'+ %.3f'  % slr.coef_[0], '* X' )

#-------- 2. Korak - Iscrtava se grafik na osnovu uzetih podataka za tacke i odredjenih koeficijenata b0 i b1
        plt.scatter(X, Y, color='red', label = 'Ostvarena produktivnost')
        plt.xlabel('Ukupno saltera u posti')
        plt.ylabel('Produktivnost')
        plt.plot(X, slr.intercept_ + slr.coef_[0] * X, color='blue', linewidth=2, label = 'Regresiona prava')   #<-- Formula Y = b0 + b1*X
        plt.grid(True)
        plt.title('Prikaz ostvarene produktivnosti i regresione prave')
        plt.legend(loc='upper right')
        plt.show()
        input('\nPress any key to continue . . .\n')

        print('\nb. Vrsimo predikciju produktivnosti ')
        attr_list = list(baza.columns.values)
        attr_list.remove('Organizaciona celina')
        attr_list.remove('Ukupno saltera u posti')
        attr_list.remove('Januar')
        attr_list.remove('Februar')
        attr_list.remove('Mart')
        attr_list.remove('April')
        attr_list.remove('Maj')
        attr_list.remove('Jun')
        attr_list.remove('Jul')
        attr_list.remove('Avgust')
        attr_list.remove('Septembar')
        attr_list.remove('Oktobar')
        attr_list.remove('Novembar')
        attr_list.remove('Prosecna produktivnost')
        X = baza[attr_list].values
        slr.fit(X, Y)

        model_coef = {'Feature': attr_list, 'LR': slr.coef_}   #  Estimated coefficients for the linear regression problem
        model_coef = pd.DataFrame(model_coef, columns=['Feature', 'LR'])
        print('\nKoeficijent modela:\n', model_coef, '\n')  # parameters of the regression line

        y_pred = slr.predict(X)   # Predict using the fitted model
        plt.scatter(Y, y_pred, c='b', label = 'Predvidjena vrednost produktivnosti')
        plt.plot([0,180],[0,180], 'r-', label = 'Regresiona prava')
        plt.xlabel('Stvarno ostvarena produktivnost')
        plt.ylabel('Predvidjene vrednost produktivnosti')
        plt.title('Predikcija vrednosti produktivnosti pomocu modela')
        plt.grid(True)
        plt.legend(loc='upper right')
        plt.show()
        input('Press any key to continue . . . \n')
#-------- 3. Korak - Evaluacija modela Linearne regresije, odredjivanje R^2, SEE, MSE ----------------------------------
        X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.6, random_state=0)
        print("c. Treniranje modela Linearne regresije \n")
        slr.fit(X_train, y_train)
        y_train_pred = slr.predict(X_train)
        y_test_pred = slr.predict(X_test)

        plt.scatter(y_train_pred, y_train_pred - y_train, c='blue', marker='o', label='Trening podaci')
        plt.scatter(y_test_pred, y_test_pred - y_test, c='lightgreen', marker='s', label='Test podaci')
        plt.title('Podaci za trening i podaci za testiranje modela')
        plt.xlabel('Predicted values')
        plt.ylabel('Residuals')
        plt.legend(loc='upper right')
        plt.hlines(y=0, xmin=0, xmax=200, lw=2, color='red')
        plt.xlim([0, 200])
        plt.tight_layout()
        plt.show()

        print('Koeficijent modela:\n', model_coef, '\n')
        model_coef['LR train'] = slr.coef_
        print(model_coef, '\n')
        input('Press any key to continue . . .\n ')

        print("d. Ocena pouzdanosti Linearne regresije ")
        print('\nOdredjujem koeficijent R^2 i greske SEE i MSE')
        r2_train = r2_score(y_train, y_train_pred)     # Coefficient of determination
        r2_test = r2_score(y_test, y_test_pred)

        mse_train = mean_squared_error(y_train, y_train_pred)  # Mean squared error regression loss
        mse_test = mean_squared_error(y_test, y_test_pred)

        see_train = math.sqrt(mse_train)  # Standard Error of Estimate
        see_test = math.sqrt(mse_test)

        model_evaluate = {'Score': ['R^2 train', 'R^2 test ', 'SEE train', 'SEE test ', 'MSE train', 'MSE test '],
                             'LR': [r2_train, r2_test, see_train, see_test, mse_train, mse_test]}
        model_evaluate = pd.DataFrame(model_evaluate, columns=['Score', 'LR'])
        print(model_evaluate, '\n')
#--------- Funkcija za interval poverenja -----------------------------------------------------------------------------
    def interval_poverenja(self):
        print('e. Interval poverenja \n')
        baza = pd.read_csv("baza.csv")
        baza.columns = ['Organizaciona celina', 'Januar', 'Februar', 'Mart', 'April',  'Maj', 'Jun', 'Jul', 'Avgust',
                        'Septembar', 'Oktobar', 'Novembar', 'Prosecna produktivnost','Stalno aktivni salteri',
                        'Povremeno aktivni salteri', 'Neaktivni salteri', 'Ukupno saltera u posti',
                        'Automatizovani salteri', 'Univerzalni salteri', 'Salteri uplata isplata']
        X = baza[['Ukupno saltera u posti']].values
        Y = baza['Prosecna produktivnost'].values
        slr = LinearRegression()
        slr.fit(X, Y)    # Fit regression model
        beta0 = slr.intercept_
        beta1 = slr.coef_
        #----- Testiranje modela Linearne Regresije --------------------------------------------------------------------
        X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.6, random_state=0)
        slr.fit(X_train, y_train)
        y_train_pred = slr.predict(X_train)
        y_test_pred = slr.predict(X_test)
        r2_train = r2_score(y_train, y_train_pred)     # Coefficient of determination
        r2_test = r2_score(y_test, y_test_pred)
        mse_train = mean_squared_error(y_train, y_train_pred)  # Mean squared error regression loss
        mse_test = mean_squared_error(y_test, y_test_pred)
        see_train = math.sqrt(mse_train)  # Standard Error of Estimate
        see_test = math.sqrt(mse_test)
#----------------- Odredjujem Interval poverenja -----------------------------------------------------------------------
        print('Uzmemo test vrednosti za X koje obelezim sa Xnovo')
        Xnovo = X_test
        Ynovo = y_test
        print('\nZatim izracunamo Y^ = bo + b1 * Xnovo')
        print('bo = %.3f' % beta0)
        print('b1 = %.3f' % beta1)
        print('\nY^ = %.3f' % beta0,'+ %.3f' % beta1, '* Xnovo')
        Ymodel = beta0 + beta1 * Xnovo
        print('\nIz Ygornje = Y^ + 2 * SEE sledi gornja granica intervala')
        Ygornje = Ymodel+2*see_train
        print('\nIz Ydonje = Y^ - 2 * SEE sledi donja granica intervala')
        Ydonje = Ymodel-2*see_train
#--------- Graficki prikaz Intervala poverenja --------------------------------------------------------------------
        print('\nf. Graficki prikaz Intervala poverenja')
        plt.scatter(Xnovo, Ynovo, color='blue', label ='Produktivnost')
        plt.plot(Xnovo, Ymodel, color='red', label ='Regresiona prava')
        plt.plot(Xnovo, Ygornje, color='green', label ='Gornja granica intervala')
        plt.plot(Xnovo, Ydonje, color='lightgreen', label ='Donja granica intervala')
        plt.legend(loc='upper right')
        plt.xlabel('Xnovo - proizvoljan broj saltera')
        plt.ylabel('Y - produktivnost')
        plt.grid(True)
        plt.title('Interval poverenja')
        plt.show()