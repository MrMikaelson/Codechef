# cook your dish here
def sol(integers,N):
    integers.sort()
    operations = 0
    for i in range(N):
        if integers[i]<i+1:
            operations += i + 1 - integers[i] 
        elif integers[i] > i+1:
            return -1
    return operations
    
T = int(input())
for _ in range(T):
    N = int(input())
    integers = list(map(int,input().split()))
    print(sol(integers,N))
    