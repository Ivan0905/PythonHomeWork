# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого набора.
# m - кол-во элементов второго набора.
# Значения генерируются случайным образом.

# Input: 11 6
# (значения сгенерированы случайным образом
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18)

# Output: 11 6
# 6 12

import random
n = int(input("Введите размер списка N: "))
m = int(input("Введите размер списка M: "))
N = list(random.randint(0, 10) for i in range(n))
M = list(random.randint(0, 10) for i in range(n))


def rez(x, y):
    print(x)
    print(y)
    Rez = set(x) & set(y)
    if (len(Rez) > 0):
        return print('Совпало: ', Rez)
    else:
        return print('Нет совпадений!')


rez(N, M)

# Задача 24:
# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.

# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

# Input: 4
# (значения сгенерированы случайным образом
# 4 2 3 1 )

# Output: 9


N = int(input("Введите кол-во кустов N: "))
List1 = list(random.randint(0, 10) for i in range(N))


def Max(MyList):
    count = list()
    for i in range(len(MyList) - 1):
        count.append(MyList[i - 1] + MyList[i] + MyList[i + 1])
    count.append(MyList[-2] + MyList[-1] + MyList[0])
    return max(count)


print(Max(List1))

# Задачи на повторение по материалам предыдущих семинаров (по желанию)
# Задача 101 Вычислить число π c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141    0.1 ≤ d ≤ 0.00000000001

import math

d = int(input("Введите кол-во знаков после запятой: "))
Mypi = round(math.pi, d)
print(Mypi)

# Задача 102 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
N = int(input("Задайте число N: "))
n = 1
MyList=list()
while n<10:
    if N%n==0:
        MyList.append(n)
        n+=1
    else:
        n+=1
print(MyList)