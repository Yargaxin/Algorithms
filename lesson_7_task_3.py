import random

arr = [random.randint(0, 100) for i in range(13)]
print(f'Array not sort: {arr}')

def simple_count_ingsort(a):
    scope = max(a) + 1
    c = [0] * scope
    
    for x in a:
        c[x] += 1
    
    a[:] = []
    
    for number in range(scope):
        a += [number] * c[number]

    return a[:]

mediana = simple_count_ingsort(arr)
print(f'Array sort: {mediana}')

ind = len(mediana) // 2
print(f'Mediana: {mediana[ind]}')