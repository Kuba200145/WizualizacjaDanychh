#Zad1
# class Materiał:
#     def __init__(self, rodzaj, długość, szerokość):
#         self.rodzaj=rodzaj
#         self.długość=długość
#         self.szerokość=szerokość
#
#     def wyświetl_nazwę(self):
#         return self.rodzaj
#
# M=Materiał('jedwab','kaszmir','bawełna')
#
# print(M.wyświetl_nazwę())

# class Ubrania:
#     def __init__(self, rozmiar, kolor, dla_kogo):
#         self.rozmiar=rozmiar
#         self.kolor=kolor
#         self.dla_kogo=dla_kogo
#
#     def wyświetl_dane(self):
#         return self.rozmiar +' '+ self.kolor +' '+ self.dla_kogo
#
# U=Ubrania('S','czerwony','kobieta')
#
# print(U.wyświetl_dane())

# class Sweter:
#     def __init__(self, rodzaj_swetra):
#         self.rodzaj_swetra=rodzaj_swetra
#
#     def wyświetl_dane(self):
#         return self.rodzaj_swetra
#
# S=Sweter('rozpinany')
#
# print(S.wyświetl_dane())

#Zad2
# class Kwadrat:
#     def __init__(self,bok,obwód):
#         self.bok=bok
#         self.obwód=obwód
#
#     def __add__(self, other):
#         nowy_bok=self.bok+self.obwód
#         return Kwadrat(nowy_bok)
#
# kwadrat=Kwadrat(5,45)
# print(kwadrat)

#Zad3
# class Kwadrat:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#
#     def __ge__(self, other):
#     return not (self < other)
#
#     def __gt__(self, other):
#     return (self > other)
#
#     def __le__(self, other):
#     return not (self > other)
#
#     def __lt__(self, other):
#     return (self < other)

#Zad4
# class Point:
#     counter = []
#
#     def __init__(self,x=0,y=0):
#         self.x=x
#         self.y=y
#
#     def update(self, n):
#         self.counter.append(n)
#
# w1=Point(1,5)
# w2=Point(2,4)
#
# print(w1.counter)
# print(w2.counter)
# w1.update(4)
# w2.update(2)
# print(w1.counter)
# print(w2.counter)

#Zad5
# class Osoba:
#     def __init__(self,imie,nazwisko):
#         self.imie=imie
#         self.nazwisko=nazwisko
#
#     def przedstaw_sie(selfs):
#         return "{} {}".format(self.imie,self.nazwisko)
#
# class Pracownik(Osoba):
#     def __init__(self,imie,nazwisko,pensja):
#         Osoba.__init__(self, imie, nazwisko)
#         self.pensja=pensja
#
#     def przedstaw_sie(self):
#         return "Jestem {} {} i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)
#
# class Menadzer(Pracownik):
#     def przedstaw_sie(self):
#         return "{} {}, jestem menadżerem i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)
#
# Andrzej = Pracownik("Andrzej", "Kowalski",3000)
# Marek = Menadzer("Marek","Nowak",13000)
#
# print(Andrzej.przedstaw_sie())
# print(Marek.przedstaw_sie())
#
# print(issubclass(Pracownik,Osoba))
# print(issubclass(Menadzer,Pracownik))
# print(isinstance(Pracownik,Osoba))
# print(isinstance(Menadzer,Pracownik))











