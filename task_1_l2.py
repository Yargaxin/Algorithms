"""
https://drive.google.com/file/d/1BI0qjwVVCUxdrZomyC_SRa629m9o6CKE/view?usp=sharing
Написать программу, которая будет складывать, вычитать, умножать или делить два числа.

"""
move = 1

while move != 0:
	move = input('What do you want to do ("+", "-", "*", "/", "0"): ')
	if move == '0':
		print('Good Luck!')
		break
	else:
		a = float(input('Input first float number: '))
		b = float(input('Input second float number: '))
		if move == '+':
			c = a + b
			print(f'Answer: {c}')

		if move == '-':
			c = a - b
			print(f'Answer: {c}')

		if move == '*':
			c = a * b
			print(f'Answer: {c}')

		if move == '/':
			if b == 0:
				print('Divison by zero!!')
				break
			c = a / b
			print(f'Answer: {c}')

		else:
			print('Wrong!')
			break