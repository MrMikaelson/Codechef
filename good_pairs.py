T = int(input())
for _ in range(T):
    N = int(input())
    A = input().split(" ")
    B = input().split(" ")
    good = 0
    for i in range(N):
        for j in range(i+1, N):
            xa = int(A[i]) ^ int(A[j])
            xb = int(B[i]) ^ int(B[j])
            if xa == xb:
                good += 1
            else:
                continue
    print(good)
