from math import exp, log

def func_obj(x):
    summation = 0
    for i in range(1, 100):
        u = 25 + (-50 * log(0.01 * i)) ** (1/1.5)
        summation += (exp(-((u - x[1])**x[2])/x[0]) - 0.01 * i) ** 2
    return summation