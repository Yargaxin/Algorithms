"""
Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел

"""
n = int(input('Input int number: '))
n_c = int(input('Input number 1-9: '))

def count_n(n, n_c):
	count = 0
	n_copy = n
	while n != 0:
		last = n % 10
		if last == n_c:
			count += 1

		n //= 10

	return f'Number {n_c} occurs {count} times in number {n_copy}'

print(count_n(n, n_c))