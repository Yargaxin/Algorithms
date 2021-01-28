"""
Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

"""


n = int(input('Input int number: '))

def even_num(n):
	c_e = 0
	c_o = 0

	while n != 0:
		last_n = n % 10
		if last_n % 2 == 0:
			c_e += 1
		else:
			c_o += 1

		n //= 10

	return f'Odd: {c_o}, Even: {c_e}'

print(even_num(n))	