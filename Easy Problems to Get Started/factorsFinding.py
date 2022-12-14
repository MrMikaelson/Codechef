import math
N = int(input())
factors = []
i = 1
while i*i <= N:
    if N % i == 0:
        factors.append(i)
    if N//i != i: 
        factors.append(N//i)
    i += 1

factors.sort()
factors.insert(0,len(factors))
print(*factors)