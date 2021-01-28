"""
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. 
Например, если введено число 3486, надо вывести 6843.

"""

n = int(input('Input int number: '))

def reverse_num(n):
	new_num = ''
	while n != 0:
		last = n % 10
		new_num += str(last)
		n //= 10

	return f'New number: {new_num}'

print(reverse_num(n))