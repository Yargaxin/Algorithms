"""
Во втором массиве сохранить индексы четных элементов первого массива.

"""

n = int(input('Input amount number: '))
a = [int(input('Input int number: ')) for i in range(n)]
b = []

for i in range(len(a)):
	if a[i] % 2 == 0:
		b += [i]		

print(b)