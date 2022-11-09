import math

tol = 1e-1
itlimit = 7

def f(x):
    return x ** 3 -3*x -4

def df(x):
    return  3*x**2-3

def newton(x1,it=1):
    x2 = x1 - f(x1)/df(x1)
    print('iteration #'+str(it)+": "+str(x1)+'   '+str(x2)+'   '+str(abs(x2-x1)))
    if (abs(f(x2)-f(x1)) < tol):
        return x2
    return newton(x2,it+1)

def bisection(a,b,it=1):
    c = (a+b)/2
    print('iteration #'+str(it)+": "+str(a)+'   '+str(b)+'   '+str(abs(f(c))))
    if abs(f(c)) < tol:
        return c
    elif f(a) * f(c) < 0:
        return bisection(a,c,it+1)
    else:
        return bisection(c,b,it+1)

def secant(a,b,it=1):
    c = b - f(b)*(b-a)/(f(b)-f(a))
    print('iteration #'+str(it)+": "+str(b)+'   '+str(c)+'   '+str(abs(c-b)))
    if abs(c-b) < tol:
        return c
    return secant(b,c,it+1)

print('Bisection:')
print(bisection(0,3))

print('Secant')
print(secant(0,3))

tol = 1e-6
print('Newton:')
print(newton(3))

