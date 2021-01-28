"""
Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
"""

def print_asc(s1, s2):
	if s1 == s2:
		return chr(s1)
	else:
		return f'{s1} = {chr(s1)} {print_asc(s1 + 1, s2)}'

print(print_asc(32, 127))