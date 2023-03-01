# cook your dish here
import math
def smallestDivisor(n):
    if (n % 2 == 0):
        return 2;
    i = 3;
    while(i * i <= n):
        if (n % i == 0):
            return i;
        i += 2;
    return n;

for _ in range(int(input())):
    X,Y = input().split()
    X = int(X)
    Y = int(Y)
    t = 0
    while(X%2!=0):
        X = X + smallestDivisor(X)
        t+=1
    t += ((Y-X)/2)
    print(math.ceil(t))