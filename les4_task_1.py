"""
Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков

"""
import timeit
import math

def fac(n):
    """
    Функция поиска факториала числа n циклом for
    """

    factorial = 1
    for i in range(2, n+1):
        factorial *= i

    return factorial


def fac_rec(n):
    """
    Функция поиска факториала числа n с помощью рекурсии
    """

    if n == 0:
        return 1

    else:
        return fac_rec(n-1) * n

def fac_math(n):
    """
    Функция поиска факториала с помощью функции math и метода factorial
    """
    return math.factorial(n)


time_for_fac = timeit.timeit('fac(950)', number=100, globals=globals())
time_met_fac = timeit.timeit('fac_math(950)', number=100, globals=globals())
time_rec_fac = timeit.timeit('fac_rec(950)', number=100, globals=globals())


print(time_for_fac) # 0.0831559
print(time_rec_fac) # 0.1159675
print(time_met_fac) #0.027282600000000018

print(f'Программа с методом factorial быстрее программы с for в {round(time_for_fac / time_met_fac, 2)} раза')
print(f'Программа с методом factorial быстрее программы с рекурсией в {round(time_rec_fac / time_met_fac, 2)} раза')
print(f'Программа с методом for быстрее программы с рекурсией в {round(time_rec_fac / time_for_fac, 2)} раза')

print('Самая быстрая программа это с методом factorial библиотеки math.')