_author_='Tamara'

import sys
import os
import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats

class Klasa2:
#------------ Funkcije za opciju 4 --------------------------------------------------------------------------------
    def kljucne_varijable(self):
        print('\na. Parovi grafikona koji opisuju vezu izmedju kljucnih varijabli')
        baza = pd.read_csv("baza.csv")
        baza.columns = ['Organizaciona celina', 'Januar', 'Februar', 'Mart', 'April',  'Maj', 'Jun', 'Jul', 'Avgust',
                        'Septembar', 'Oktobar', 'Novembar', 'Prosecna produktivnost','Stalno aktivni salteri',
                        'Povremeno aktivni salteri', 'Neaktivni salteri', 'Ukupno saltera u posti',
                        'Automatizovani salteri', 'Univerzalni salteri', 'Salteri uplata isplata']

        sns.pairplot(baza, vars=['Ukupno saltera u posti', 'Prosecna produktivnost'])    # Plot a subset of variables
        print('working ...')
        plt.show()

        sns.pairplot(baza, vars=['Stalno aktivni salteri', 'Prosecna produktivnost'])    # Plot a subset of variables
        print('working ...')
        plt.show()

        sns.pairplot(baza, vars=['Automatizovani salteri', 'Prosecna produktivnost'])    # Plot a subset of variables
        print('working ...')
        plt.show()

        sns.pairplot(baza, vars=[ 'Univerzalni salteri', 'Prosecna produktivnost'])    # Plot a subset of variables
        print('working ...')
        plt.show()

        sns.pairplot(baza, vars=[ 'Salteri uplata isplata', 'Prosecna produktivnost'])    # Plot a subset of variables
        print('working ...')
        plt.show()

        sns.pairplot(baza, vars=['Ukupno saltera u posti', 'Automatizovani salteri',
                                 'Univerzalni salteri', 'Salteri uplata isplata', 'Prosecna produktivnost'], diag_kind='kde')    # Kernel density estimates for univariate plots
        print('working ...')
        plt.show()

        sns.pairplot(baza, vars=['Ukupno saltera u posti', 'Automatizovani salteri',
                                 'Univerzalni salteri', 'Salteri uplata isplata', 'Prosecna produktivnost'], kind='reg')    # Fit linear regression models to the scatter plots
        print('working ...')
        plt.show()
#---------------------------------------------------------------------------------------------------------------------
    def univarijantna_raspodela(self):
        baza = pd.read_csv("baza.csv")
        baza.columns = ['Organizaciona celina', 'Januar', 'Februar', 'Mart', 'April',  'Maj', 'Jun', 'Jul', 'Avgust',
                        'Septembar', 'Oktobar', 'Novembar', 'Prosecna produktivnost','Stalno aktivni salteri',
                        'Povremeno aktivni salteri', 'Neaktivni salteri', 'Ukupno saltera u posti',
                        'Automatizovani salteri', 'Univerzalni salteri', 'Salteri uplata isplata']

        print('b. Prikaz bivarijantne raspodele ')
        g = sns.JointGrid('Ukupno saltera u posti', 'Prosecna produktivnost', baza)
        g.plot_marginals(sns.distplot, kde=False, color=".5")
        g.plot_joint(plt.scatter, color=".5", edgecolor="white")
        g.annotate(stats.pearsonr, template="{stat} = {val:.3f} (p = {p:.3g})");
        plt.show()

        g = sns.JointGrid('Automatizovani salteri', 'Prosecna produktivnost', baza)
        g.plot_marginals(sns.distplot, kde=False, color=".5")
        g.plot_joint(plt.scatter, color=".5", edgecolor="white")
        g.annotate(stats.pearsonr, template="{stat} = {val:.3f} (p = {p:.3g})");
        plt.show()

        g = sns.JointGrid('Univerzalni salteri', 'Prosecna produktivnost', baza)
        g.plot_marginals(sns.distplot, kde=False, color=".5")
        g.plot_joint(plt.scatter, color=".5", edgecolor="white")
        g.annotate(stats.pearsonr, template="{stat} = {val:.3f} (p = {p:.3g})");
        plt.show()

        g = sns.JointGrid('Salteri uplata isplata', 'Prosecna produktivnost', baza)
        g.plot_marginals(sns.distplot, kde=False, color=".5")
        g.plot_joint(plt.scatter, color=".5", edgecolor="white")
        g.annotate(stats.pearsonr, template="{stat} = {val:.3f} (p = {p:.3g})");
        plt.show()