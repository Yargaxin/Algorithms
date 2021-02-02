"""
В одномерном массиве целых чисел определить два наименьших элемента.

"""

import random

a = [random.randint(1, 1001) for i in range(10)]
min_v = 1000
min_v_2 = 1000
l = []

for j in a:
	if j < min_v:
		min_v = j

ind_min = 0

for x in range(len(a)):
	if a[x] == min_v:
		ind_min = x

l.append(min_v)

del a[ind_min]

for i in a:
	if i < min_v_2:
		min_v_2 = i

l.append(min_v_2)

print(a)
print(f'List of minimal value: {l}')