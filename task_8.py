"""
Определить, является ли год, который ввел пользователь, високосным или не високосным.

"""


y = int(input('Input year: '))

if (y % 4 == 0) and (y % 100 != 0) or (y % 400 == 0):
	print('Leap year')

else:
	print('Not leap year')