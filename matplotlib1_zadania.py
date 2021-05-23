import numpy as np
import matplotlib.pyplot as plt
import math
import xlrd
import openpyxl
import pandas as pd

#Zad1
# x = np.arange(20,40,1)
# plt.xlabel('x')
# plt.ylabel('f(x)')
#
# plt.plot(x, 1/x, label="wymierna")
# plt.legend()
# plt.show()

#Zad2
# x = np.arange(20,40,1)
# plt.xlabel('x')
# plt.ylabel('1/x')
# plt.title('Wykres funkcji f(x) dla x[20,40]')
#
# plt.plot(x, 1/x,'b.--')
# plt.show()

#Zad3
# x = np.arange(0,45,0.1)
# s = np.sin(x)
# c = np.cos(x)
# plt.xlabel('x')
# plt.ylabel('sin(x)  cos(x)')
# plt.title('Wykres funkcji sin(x), cos(x)')
# plt.plot(x, s, label="sin(x)")
# plt.plot(x, c, label="cos(x)")
# plt.legend()
# plt.show()

#Zad4
# x = np.arange(0,45,0.1)
# s = np.sin(x)
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# plt.title('Wykres funkcji sin(x)')
# plt.plot(x, s+1, label="sin(x)")
# plt.plot(x, -s-1, label="sin(x)")
# plt.legend()
# plt.show()

#Zad5
# x=[4.3,7.9,5.84,0.83]
# y=[2.0,4.4,3.05,0.43]
# s= abs(np.subtract(x,y))
#
# plt.scatter(x,y,c=x)
#
# plt.xlabel('sepal length')
# plt.ylabel('sepal width')
# plt.title('Iris')
# plt.show()
# print('wartość absolutna x-y')
# print(s)

#Zad6
#WYKRES 1

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

#WYKRES 3

# xlsx= pd.ExcelFile('imiona.xlsx')
# df= pd.read_excel(xlsx, header=0)
#
# etykiety=['2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']
# wartosci= df.groupby('Rok')['Liczba'].sum()
# print(wartosci)
#
# plt.bar(etykiety,wartosci)
#
# plt.xlabel('Rok')
# plt.ylabel('Ilość narodzin')
#
# plt.show()

#Zad7
# df=pd.read_csv('zamowienia.csv',header=0, sep=';',decimal='.')
#
# wartosci= df.groupby('Sprzedawca').count()
# print(wartosci)
#
# czesci=[99,117,41,92,67,42,125,151,65]
# sprzedawcy=['Callahan','Davolio','Dudek','Fuller','King','Kowalski','Laverling','Peacock','Swiński']
#
#
# plt.pie(czesci,labels=sprzedawcy,startangle=90,explode=(0,0,0,0,0,0,0,0.1,0),autopct='%1.1f%%')
#
# plt.title('Wykres kołowy sprzedawców w ogólnej liczbie zamówień')
# plt.show()
