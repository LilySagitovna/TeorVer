# В ящике имеется 15 деталей, из которых 9 окрашены. Рабочий случайным образом извлекает 3 детали.
# Какова вероятность того, что все извлеченные детали окрашены?

from math import factorial
import numpy as np

n = 15
k = 9
details = 3

def combinations(n,k):
    return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n-k))

all_var = combinations(n,k)
painted_details = combinations(k,details)
result = painted_details / all_var
print('Вероятность того,что все детали окрашены:', result)