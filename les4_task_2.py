"""
Написать два алгоритма нахождения i-го по счёту простого числа.

"""
import timeit
import math

def get_prime_num(n):
    lst = []
    for i in range(2, n+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            lst.append(i)

    return lst

def sieve_eratosthenes(n):
    """
    Функция поиска n-го простого числа, используя алгоритм Решета Эратосфена.

    """
    sieve = list(range(n + 1))
    sieve[1] = 0 
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    
    return sieve

time_p = timeit.timeit(f'get_prime_num(1000)', number=100, globals=globals())
time_sieve_erat = timeit.timeit(f'sieve_eratosthenes(1000)', number=100, globals=globals())

print(f'Время алгоритма без <Решеты Эратосфена> {time_p} секунд') # 1.439759
print(f'Время алгоритма c <Решетой Эратосфена> {time_sieve_erat} секунд') # 0.04656919999999998

print(f'Алгоритм "Решета Эратосфена" быстрее алгоритма простого в {round(time_p / time_sieve_erat, 2)} раза')