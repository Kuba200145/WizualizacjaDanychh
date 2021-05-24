import pandas as pd
import numpy as np
import xlrd
import openpyxl
import matplotlib.pyplot as plt

#Zad1
# xlsx = pd.ExcelFile('imiona.xlsx')
# wartosci = pd.read_excel(xlsx, header=0)
# print(wartosci)

#Zad2
# print(wartosci[wartosci['Liczba']>1000])

# print(wartosci[wartosci['Imie']=='JAKUB'])

# print(wartosci.agg('Liczba').sum())


# print(wartosci[wartosci['Rok'] >= 2006].agg({'Liczba':['sum']}))


# print(wartosci.groupby('Plec')['Liczba'].sum())

#Zad3
# wartosci=pd.read_csv('zamowienia.csv',header=0, sep=';',decimal='.')

# print(wartosci['Sprzedawca'].unique())

# print(wartosci.groupby(['Sprzedawca'])[['Data zamowienia']].count())

# print(wartosci.groupby(['Kraj'])[['Utarg']].sum())

# print(wartosci[((wartosci['Data zamowienia'] >= '2005-01-01') & (wartosci['Data zamowienia'] <= '2005-12-31') & (wartosci['Kraj'] == 'Polska'))].agg({'Utarg':['sum']}))

# print(wartosci[((wartosci['Data zamowienia'].str[:4] == '2004'))]['Utarg'].mean())




