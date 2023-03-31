#Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)


def numbers(n):
    print("Введите элементы массива:")
    n_list = list()
    for i in range(n):
        number = int(input())
        n_list.append(number)
    return n_list

def searchIndex(a, b, n, n_list):
    index = list()
    for i in range(0, n):
        if ((a-1) < n_list[i] < (b+1)):
            index.append(i)
    return index


n = int(input("Введите количество элементов в массиве: "))
a = int(input("Введите начало диапазона: "))
b = int(input("Введите конец диапазона: "))

numbers_list = list()
numbers_list = numbers(n)

print(f'Индексы: {searchIndex(a, b, n, numbers_list)}')