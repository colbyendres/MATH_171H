import math

tol = 1e-7
itlimit = 50

def f(x):
    return x ** 2 - 2

def df(x):
    return  2*x

def newton(x1):
    if (abs(f(x1)) < tol):
        return x1
    x2 = x1 - f(x1)/df(x1)
    return newton(x2)

def bisection(a,b):
    c = (a+b)/2
    if abs(f(c)) < tol:
        return c
    elif f(a) * f(c) < 0:
        return bisection(a,c)
    else:
        return bisection(c,b)

def secant(x1,x2):
    x3 = x1 - f(x1) * (x1-x2)/(f(x1)-f(x2))
    if (abs(f(x3)) < tol):
        return x3
    return secant(x2,x3)

print(newton(2))
print(bisection(1,2))
print(secant(1,2))
print(math.sqrt(2))