# На входной двери подъезда установлен кодовый замок, содержащий десять кнопок с цифрами от 0 до 9.
# Код содержит три цифры, которые нужно нажать одновременно. Какова вероятность того, что человек,
# не знающий код, откроет дверь с первой попытки?

from math import factorial
import numpy as np

n = 10
k = 3

def combi(n,k):
    return np.math.factorial(n) // np.math.factorial(k) * np.math.factorial(n-k)

print('Вероятность того, что человек не знающий код откроет дверь с первого раза: ',1/combi(n,k))
