# cook your dish here
for _ in range(int(input())):
    N = int(input())
    B = input().split()
    mod = 0
    for i in B:
        if int(i) != 0:
            mod += 1
    mod = mod%2
    if mod == N%2:
        print("YES")
    else:
        print("NO")