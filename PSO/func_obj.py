from math import exp, log

def func_obj(x):
    summation = 0
    for i in range(1, 100):
        u = 25 + (-50 * log(0.01 * i)) ** (1/1.5)
        summation += (exp(-((u - x[1])**x[2])/x[0]) - 0.01 * i) ** 2
    return summation

# print(func_obj([50, 25, 1.5])) # 0.1 <= x1 <= 100 & 0 <= x2 <= 25.6 & 0 <= x3 <= 5
