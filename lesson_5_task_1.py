import collections

try:
	c_comp = int(input('Enter the number of companies: '))
except:
	print('Mistake')

companies = []

for i in range(c_comp):
	name_comp = input('Input name company: ')
	profit_quarters = input('Enter 4 quarter profile: ').split()

	company = {
			
			'title': name_comp,
			'Profit First Quarter': int(profit_quarters[0]),
			'Profit Second Quarter': int(profit_quarters[1]),
			'Profit Third Quarter': int(profit_quarters[2]),
			'Profit Fourth Quarter': int(profit_quarters[3]),
			'Profit Year': int(profit_quarters[0]) + int(profit_quarters[1]) + int(profit_quarters[2]) + int(profit_quarters[3])

	}
	
	companies.append(company)

profit_coll = collections.Counter()
for c in companies:
	profit_c = c.copy()
	del profit_c['title']
	profit_coll += collections.Counter(profit_c)

average_p = profit_coll['Profit Year'] / len(companies) # средняя прибыль (за год для всех предприятий) 

print()
for i in companies:
	print(i)

print(f'Total profit of companies: {profit_coll}')
print(f'Average annual profit of companies: {average_p}')

above = []
below = []

for c in companies:
	if c['Profit Year'] >= average_p:
		above.append(c['title'])

	elif c['Profit Year'] < average_p:
		below.append(c['title'])

print(f'Companies with above average profits: {above}')
print(f'Companies with below average profits: {below}')
