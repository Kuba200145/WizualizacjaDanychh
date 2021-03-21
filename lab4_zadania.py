# #Zad1
# import random
# losowanie=[]
# for i in range(50):
#     los = random.randint(0, 200)
#     if los % 4 == 0:
#         losowanie.append(los)
# plik=open('LiczbyPodzielnePrzez4.txt','a+')
# for liczba in losowanie:
#     plik.write(str(liczba)+'\n')
# plik.close()

#Zad2
# plik = open('LiczbyPodzielnePrzez4.txt','r')
# wszystko= plik.readlines()
# print(wszystko)

#Zad3
# with open('LiczbyPodzielnePrzez4.txt','r') as plik:
#     for linia in plik:
#         print(linia,end='')

#Zad4
# class NaZakupy:
#     def metoda(self,nazwa_produktu, ilosc, jednostka_miary, cena_jed):
#         self.nazwa_produktu=nazwa_produktu
#         self.ilosc=ilosc
#         self.jednostka_miary=jednostka_miary
#         self.cena_jed=cena_jed
#     def wyswietl_produkt(self):
#         return self.nazwa_produktu
#     def ile_produktu(self):
#         return self.ilosc + self.jednostka_miary
#     def ile_kosztuje(self):
#         return self.ilosc * self.cena_jed
#
# zakupy=NaZakupy('listaZakupow')
#
# print(zakupy.wyswietl_produkt())
# print(zakupy.ile_kosztuje())
# print(zakupy.cena_jed)
# print(zakupy.ilosc)

#Zad6
# class Robaczek:
#     def __init__(self,x,y,krok):
#         self.x=x
#         self.y=y
#         self.krok=krok
#
#     def idz_w_gore(self,ile_krokow):
#         self.y+=ile_krokow*self.krok
#
#     def idz_w_dol(self,ile_krokow):
#         self.y-=ile_krokow*self.krok
#
#     def idz_w_lewo(self,ile_krokow):
#         self.x-=ile_krokow*self.krok
#
#     def idz_w_prawo(self,ile_krokow):
#         self.x+=ile_krokow*self.krok
#
#     def pokaz_gdzie_jestes(self):
#         return (self.x,self.y)
#
# Dżdżownica=Robaczek(10,10,10)
#
# Dżdżownica.idz_w_gore(20)
# print(Dżdżownica.pokaz_gdzie_jestes())
# Dżdżownica.idz_w_dol(30)
# print(Dżdżownica.pokaz_gdzie_jestes())
# Dżdżownica.idz_w_lewo(40)
# print(Dżdżownica.pokaz_gdzie_jestes())
# Dżdżownica.idz_w_prawo(50)
# print(Dżdżownica.pokaz_gdzie_jestes())










