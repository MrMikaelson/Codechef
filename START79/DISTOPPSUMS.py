# cook your dish here
for _ in range(int(input())):
    N = int(input())
    P = []
    for i in range(int(N/2),0,-1):
        P.append(i)
    for i in range(int(N/2)+1,N+1):
        P.append(i)
    print(*P)
    