# cook your dish here
for _ in range(int(input())):
    for _ in range(int(input())):
        I,N,Q = map(int, input().split())
        if N%2==0:
            print(N/2)
        else:
            if I == Q:
                print(N//2)
            else:
                print((N//2)+1)