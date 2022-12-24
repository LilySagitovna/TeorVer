# В лотерее 100 билетов. Из них 2 выигрышных. Какова вероятность того,
# что 2 приобретенных билета окажутся выигрышными?

from math import factorial
import numpy as np
n = 100
k = 2
purchased_ticket = 2


def combi(n, k):
    return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))


all_result = combi(n, k)  # всего сочетаний
winning_result = combi(k, purchased_ticket)
ver_winning_ticket = winning_result / all_result
print("Вероятность того, что 2 приобретенных билета окажутся выигрышными:", ver_winning_ticket)
