"""
По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, 
составленного из этих отрезков.

Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.
"""

a = int(input('Input first side of a triangle: '))
b = int(input('Input second side of a triangle: '))
c = int(input('Input third side of a triangle: '))

if a + b > c and a + c > b and b + c > a:
	if a == b == c:
		print('The triangle exists')
		print('The triangle = Equilateral')
	
	elif a == b or a == c or b == c:
		print('The triangle exists')
		print('The triangle = Isosceles')

	else:
		print('The triangle exists')
		print('The triangle = Versatile')

else:
	print('The triangle does not exists')