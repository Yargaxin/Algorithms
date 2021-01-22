"""Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
https://drive.google.com/file/d/1gtU3hFgf4HtjbFM6FCiiXUqnBWLyc2Ve/view?usp=sharing

"""

n = int(input('Input three-digit number: '))

s = 0
mult = 1

n_3 = n % 10
n_2 = (n // 10) % 10
n_1 = n // 100

s += n_3 + n_2 + n_1
mult *= n_3 * n_2 * n_1

print(f'Sum number {n} = {s}')
print(f'Multiple number {n} = {mult}')