import math

def f(x):
    return x ** 3

def LHRectangle(a,b,n):
    width  = (b-a)/n
    area = 0

    for i in range(n): # Skip last point
        area += width * f(a+i*width)

    return area

def RHRectangle(a,b,n):
    width  = (b-a)/n
    area = 0

    for i in range(n): # Skip first point
        area += width * f(b-i*width)

    return area

def trapRule(a,b,n):
    width =  (b-a)/n
    area = f(a)+f(b) # First and last endpoints have weight 1
    
    for i in range(1,n):
        area += 2 * f(a+i*width)
    
    return area * width / 2

def simpsonsRule(a,b,n):
    width = (b-a)/n
    area = f(a) + f(b) # First and last endpoints have weight 1
    mult = 1

    for i in range(1,n):
        if i % 2 == 0:
            mult = 2
        else:
            mult = 4
        area += mult * f(a+i*width)

    return area * width / 3

# Driver code
a = 0
b = 1

I10 = LHRectangle(0,1,10)
I20 = LHRectangle(0,1,20)
print('left (n=10):',I10)
print('left (n=20):',I20)
print('2I20 - I10:',2*I20-I10,'\n')

I10 = RHRectangle(0,1,10)
I20 = RHRectangle(0,1,20)
print('right (n=10):',I10)
print('right (n=20):',I20)
print('2I20 - I10:',2*I20-I10,'\n')

I10 = trapRule(0,1,10)
I20 = trapRule(0,1,20)
print('trapezoid (n=10):',I10)
print('trapezoid (n=20):',I20)
print('2I20-I10:',2*I20-I10)
print('(4I20-I10)/3:',(4*I20-I10)/3,'\n')

I10 = simpsonsRule(0,1,10)
I20 = simpsonsRule(0,1,20)
print('Simpson\'s (n=10):',I10)
print('Simpson\'s (n=20):',I20)
print('(16I20-I10)/15',(16*I20-I10)/15)

# Brute force through all powers of two
two_pow = 2
BIG_NUM = 15

for i in range(BIG_NUM):
    diff = (two_pow*I20-I10)/(two_pow-1)
    print([i,diff])
    two_pow <<= 1
