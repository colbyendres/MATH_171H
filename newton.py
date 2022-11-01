import math

tol = 1e-1
itlimit = 50

def f(x):
    return x ** 3 -3*x -4

def df(x):
    return  3*x**2-3

def newton(x1,it=0):
    x2 = x1 - f(x1)/df(x1)
    print(x1,x2,abs(f(x2)-f(x1)))
    if (abs(f(x2)-f(x1)) < tol):
        return x2
    return newton(x2,it+1)

def bisection(prev,a,b,it=0):
    c = (a+b)/2
    print("it", it,"",[a,b])
    if abs(f(c)) < tol:
        return c
    elif f(a) * f(c) < 0:
        return bisection(f(c),a,c,it+1)
    else:
        return bisection(f(c),c,b,it+1)

def secant(x1,x2,it=0):
    x3 = x1 - f(x1) * (x1-x2)/(f(x1)-f(x2))
    print([x2,x3,abs(f(x2)-f(x3))])
    if (abs(f(x3)-f(x2)) < tol):
        return x3
    return secant(x2,x3,it+1)

# Garbage value
prev = 1e5

# print(newton(3))
# print(bisection(prev,0,3))
print(secant(0,3))

# Compare to math library
print(math.sqrt(2))