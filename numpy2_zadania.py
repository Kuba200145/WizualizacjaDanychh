import numpy as np

#Zad1
# a=np.array([2,3,4])
# b=np.array([6,7,8])
# print(a,b)
# print(a @ b)

#Zad2
# print('Macierz 3x3')
# a=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(a)
# print('minimum kazdej kolumny')
# print(a.min(axis=0))
# print('minimum kazdego rzedu')
# print(a.min(axis=1))
#
# print('Macierz 4x4')
# b=np.array([[3,7,9,5],[4,6,2,8],[5,4,1,4],[1,9,5,2]])
# print(b)
# print('minimum kazdej kolumny')
# print(b.min(axis=0))
# print('minimum kazdego rzedu')
# print(b.min(axis=1))

#Zad3
# a=np.array([2,3,4])
# b=np.array([6,7,8])
# print(a,b)
# print(a.dot(b))

#Zad4
# a=np.array([-7,3,-3])
# b=np.array([6.5,-7,8])
# print(a,b)
# print(a.dot(b))

#Zad5
# b=np.array([[1,8,-3],[2,-5,7]])
# print(b)
# print('wartosci sin')
# a=np.sin(b)
# print(a)

#Zad6
# a=np.array([[1,8,-3],[2,-5,7]])
# print(a)
# print('wartosci cos')
# b=np.cos(a)
# print(b)

#Zad7
# a=np.array([2,3,4])
# b=np.array([6,7,8])
#
# c=a+b
# print(c)
#
# print(np.add(a,b))

#Zad8
# a= np.arange(9).reshape(3,3)
# for b in a:
#     print(b)
#     print("")
#

#Zad9
# a= np.arange(9).reshape(3,3)
# for b in a.flat:
#     print(b)
#     print("")

#Zad10
# a= np.arange(81).reshape(9,9)
# print(a)
#
# b=a.reshape((27,3))
# print(b)
# print(b.shape)
#
# c=a.reshape((3,27))
# print(c)
# print(c.shape)

#Mamy mozliwosc zmiany macierzy 9x9 tylko na 27x3 i 3x27, poniewaz 9x9,27x3,3x27 to jedyne pary liczb które po przemonozeniu dadzą nam 81.

#Zad11
# print("Macierz 1x12")
# a=np.arange(12)
# print(a)
# print("Macierz 3x4")
# b=a.reshape((3,4))
# print(b)
# print("Macierz 4x3")
# c=a.reshape((4,3))
# print(c)
# print("Macierz 2x6")
# d=a.reshape((2,6))
# print(d)
#
# print("_________")
# for b in a.flat:
#     print(b)
# print("_________")
# for c in a.flat:
#     print(c)
# print("_________")
# for d in a.flat:
#     print(d)
# print("Wszystkie po spłaszczeniu są takie same.")

