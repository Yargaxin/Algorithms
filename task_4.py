""" 
Написать программу, которая генерирует в указанных пользователем границах: ● случайное целое число, 
● случайное вещественное число, ● случайный символ.

"""

import random

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
