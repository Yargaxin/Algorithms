"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.

"""
import random

a = [random.randint(1, 1001) for i in range(16)]
min_v = 1000
max_v = 0

for j in a:
	if j < min_v:
		min_v = j

	elif j > max_v:
		max_v = j

ind_min = 0
ind_max = 0

for x in range(len(a)):
	if a[x] == min_v:
		ind_min = x
	elif a[x] == max_v:
		ind_max = x	

s_a = a[ind_min+1:ind_max]
c = 0
for i in s_a:
	c += i

print(f'Sum: {c} | List: {s_a}')