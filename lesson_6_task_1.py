import sys
import random

""" Версия Python: python 3.8.2 x64
ОС: Windows 10 x64 """


#1)Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

a = input('Enter a three-digit number:')

x = int(a[0])
y = int(a[1])
z = int(a[2])

sum_l = x + y + z
mult = x * y * z

sum_member = sys.getsizeof(a) + sys.getsizeof(x) + sys.getsizeof(y) + sys.getsizeof(z) + sys.getsizeof(
    sum_l) + sys.getsizeof(mult)

print(f'The program uses a byte of memory: {sum_member}')

# Результат запуска программы и измерения:
# Введите трехзначное число: 567
# В программе задействовано байт памяти: 98

# ===============================================

""" 
#2)Написать программу, которая генерирует в указанных пользователем границах: ● случайное целое число, 
#● случайное вещественное число, ● случайный символ.

"""

n_1 = int(input('Input first int number: '))
n_2 = int(input('Input second int number: '))

f_1 = float(input('Input first float number: '))
f_2 = float(input('Input second float number: '))

s_1 = input('Input first symbol a-z: ')
s_2 = input('Input second symbol a-z: ')

ord_s1 = ord(s_1)
ord_s2 = ord(s_2)

print(random.randint(n_1, n_2))
print(random.uniform(f_1, f_2))
print(chr(random.randint(ord_s1, ord_s2)))

sum_member_2 = sys.getsizeof(n_1) + sys.getsizeof(n_1) + sys.getsizeof(n_1) + sys.getsizeof(n_1)+ sys.getsizeof(n_1) + sys.getsizeof(n_1) + sys.getsizeof(n_1) + sys.getsizeof(n_1)

print(f'The program uses a byte of memory: {sum_member_2}')

# Результат запуска программы и измерения:
# Input first int number: 4
# Input second int number: 56
# Input first float number: 10.4
# Input second float number: 20.5
# Input first symbol a-z: b
# Input second symbol a-z: x

# В программе задействовано байт памяти: 112


# =====================================================

#3)Во втором массиве сохранить индексы четных элементов первого массива.


n = int(input('Input amount number: '))
a = [random.randint(1, 100) for j in range(n)]
print(f'Array: {a}')

b = [i for i in range(len(a)) if a[i] % 2 == 0]
print(f'Array of even indices of list a: {b}')

sum_member_3 = sys.getsizeof(n) + sys.getsizeof(a) + sys.getsizeof(b)

print(f'The program uses a byte of memory: {sum_member_3}')

# Дан массив элементов: [74, 33, 82, 7, 69, 88, 51, 50, 66]
# Чётные индексы массив:  [0, 2, 5, 7, 8]


# type(a)=<class 'list'>, size=64, object=[74, 33, 82, 7, 69, 88, 51, 50, 66]
#	 type=<class 'int'>, size=14, object=74
#	 type=<class 'int'>, size=14, object=33
#	 type=<class 'int'>, size=14, object82
#	 type=<class 'int'>, size=14, object=7
#	 type=<class 'int'>, size=14, object=69
#	 type=<class 'int'>, size=14, object=88
#	 type=<class 'int'>, size=14, object=51
#	 type=<class 'int'>, size=14, object=50
#	 type=<class 'int'>, size=14, object=66


# Результат запуска программы и измерения:
# Input amount number: 9

# В программе задействовано байт памяти: 166 (иногда выводит 150 если список b <= 4)

"""
Итог: Первое задание и Второе будет самым эффективным, их потребление памяти будет константным
  		и предсказуемым за счет заранее определенных размеров переменных.Третья программа требует памяти больше всего

"""