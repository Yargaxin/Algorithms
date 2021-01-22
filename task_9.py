"""
Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

"""

a = int(input('Input first int number: '))
b = int(input('Input second int number: '))
c = int(input('Input third int number: '))

s = 0

if (a > b) and (a < c) or (a < b) and (a > c):
	s = a
	print(s)

else:
	if (b > a) and (b < c) or (b < a) and (b > c):
		s = b
		print(s)

	else:
		s = c
		print(s)