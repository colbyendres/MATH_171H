from math import sqrt

theta = -.5
N = 10
arr = N * [theta]

for fail in range(1,N):
    arr[0] = -2 / fail
    for i in range(1,N):
        if abs(arr[i-1]+2) < 1e-6:
            break
        arr[i] = arr[i-1]/(1+arr[i-1]/2)
    print("N = ",fail," ",arr)