# cook your dish here
T = int(input())
for _ in range(T):
    N = int(input())
    i = input().split(" ")
    a = int(i[0])
    j = 0
    for n in range(N-1):
        if int(i[n]) > int(i[n+1]):
            j = 1
        else:
            continue
    if j == 1:
        print("NO")
    elif j == 0:
        print("YES")
