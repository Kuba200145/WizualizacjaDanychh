
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Zad1
# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)
# wartosci = df.groupby('Rok')['Liczba'].sum()
# etykiety=['2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']
# print(wartosci)
# plt.plot(etykiety,wartosci)
# plt.ylabel('Liczba')
# plt.xlabel('Rok urodzenia')
# plt.title('Liczba dzieci urodzonych w danym roku')
# plt.show()

#Zad2
# xlsx= pd.ExcelFile('imiona.xlsx')
# df= pd.read_excel(xlsx, header=0)
#
# etykiety=['Kobiety','Mężczyźni']
# wartosci= df.groupby('Plec')['Liczba'].sum()
# print(wartosci)
#
# plt.bar(etykiety,wartosci)
#
# plt.xlabel('Płeć')
# plt.ylabel('Ilość narodzin')
#
# plt.show()

#Zad3
# xlsx= pd.ExcelFile('imiona.xlsx')
# df= pd.read_excel(xlsx, header=0)
# wartosci= df[df['Rok'] >= 2013].groupby(['Plec']).agg({'Liczba':['sum']})
# print(wartosci)
# explode = [0.0 for n in range(len(wartosci.index))]
# wartosci.plot.pie(subplots=True, autopct='%.2f %%', fontsize=8, explode=explode)
# plt.show()

#Zad4
# df=pd.read_csv('zamowienia.csv',header=0, sep=';',decimal='.')
# wartosci= df.groupby('Sprzedawca')['Data zamowienia'].count()
#
# sprzedawcy=['Callahan','Davolio','Dudek','Fuller','King','Kowalski','Laverling','Peacock','Swiński']
# plt.bar(sprzedawcy,wartosci)
#
# plt.show()