"""
Отсортируйте по убыванию методом пузырька.

"""

import random

arr = [random.randint(-100, 100) for i in range(10)]

def bubble_sort(arr): 
    n = len(arr) - 1
  
    for i in range(n): 
        for j in range(0, n-i):# последний уже на своём месте
            if arr[j] > arr[j+1]: 
                arr[j], arr[j+1] = arr[j+1], arr[j] 


print(f'Array not sort: {arr}')
bubble_sort(arr)
print(f'Array sort: {arr[::-1]}')