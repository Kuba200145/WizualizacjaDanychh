#Zad1
# a=[1-x for x in range(1,11)]
# b=[3**y for y in range(6)]
# c=[z for z in a if z % 2 != 1]
# print(a)
# print(b)
# print(c)

#Zad2
# liczby = [1,2,3,4,5,6,7,8,9,10]
# lista = [x for x in liczby if x%3 == 0]
# print(lista)

#Zad3
# słownik={'cukier':'kilogramy','mleko':'litry','ogórek':'sztuki'}
# wartość={key: value for value, key in słownik.items()}
# print(wartość)

#Zad4
# import math
#
# def trojkat_prostokatny(a,b,c):
#     if ((a**2+b**2==c**2) && (a**2+c**2==b**2) && (c**2+b**2==a**2)):
#         return 'Trójkąt o podanych bokach jest prostokątny'
#     else:
#         return 'Trójkat o podanych bokach nie jest prostkątny'
#
# print(trojkat_prostokatny(3,4,5))

#Zad5
# def pole_trapezu(a,b,h):
#     return (((a+b)*h)/2)
#
# print(pole_trapezu(1,2,3))

#Zad8
# def zakupy(**rzeczy):
#     return len(rzeczy.items()), sum(x for x in rzeczy.values())
# print('ilość rzeczy , łączna wartość produktów')
#
# print(zakupy(woda=2, masło=3, chleb=1.5, czekolada=2.55))



