T = int(input())
for _ in range(T):
    N, K = input().split(" ")
    N = int(N)
    K = int(K)

    if N%2==0:
        print("YES")
    else:
        if K == 1:
            print("YES")
        else:
            print("NO")