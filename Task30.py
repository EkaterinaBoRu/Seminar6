"""Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки."""

def searchNumberArithmProgress(a1, d, n):
    a = list()
    for i in range( 1, n+1):
        a.append(a1+ (i-1)*d)
    return a
    


a1 = int(input("Введите первый член арифметическоой прогрессии: "))
d = int(input("Введите разность арифметической прогрессии: "))
n = int(input("Введите число членов арифметической прогрессии: "))

a_n = tuple()
a_n = searchNumberArithmProgress(a1, d, n)

print (a_n)