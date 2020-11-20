from math import exp, log

def func_obj(x):
    summation = 0
    for i in range(1, 100):
        u = 25 + (-50 * log(0.01 * i)) ** (1/1.5)
        summation += (exp(-((u - x[1])**x[2])/x[0]) - 0.01 * i) ** 2
    return summation

def func_obj2(x):
    summation = 0
    for i in range(1, 11):
        t = 0.1 * i
        summation += ((exp(-t * x[0])) - (x[2] * exp(-t * x[1])) -  (exp(-t) - 5 * exp(10 * t))) ** 2  
    return summation

def func_obj3(x):
    a = (2*(x[0]**3)) + (5*x[0]*x[1]) + (4*x[2]) - (2*(x[0]**2)*x[2]) - 18
    b = x[0] + x[1]**3 + x[0]*(x[2]**2) - 22
    c = 8*(x[0]**2) + 2*x[1]*x[2] + 2*(x[1]**2) + 3*(x[1]**3) - 52
    fo = (a*(b**2)*c + a*b*(c**2) + b**2 + (x[0] + x[1] - x[2])**2)**2
    return fo

print(func_obj([50, 25, 1.5])) # 0.1 <= x1 <= 100 & 0 <= x2 <= 25.6 & 0 <= x3 <= 5
# print(func_obj2([1, 10, 5]))
# print(func_obj3([1, 2, 3]))
