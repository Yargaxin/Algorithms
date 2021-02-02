s = 0
for i in range(1, 20):
	s = 1
	for j in range(10, 25):
		if j % i == 0:
			s += 1

print(s)