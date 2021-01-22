"""
Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

"""

n = int(input('Input alphabet letter number: '))

abc = 'abcdefghijklmnopqrstuvwxyz'

print(abc[n-1])