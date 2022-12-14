import numpy as np

T = int(input())
for _ in range(T):
    N, K = input().split(" ")
    N = int(N)
    K = int(K)

    mat = np.zeros((N, N), dtype=int)

    for i in range(N):
        for j in range(N):
            mat[i, j] = (i+1)+(N*(j))

    number1 = 0
    operation = 0
    i = 0
    j = 0
    while i < N and j < N:
        number1 += mat[i][j]
        if operation % 2 == 0:
            j = j+1
        else:
            i = i+1
        operation += 1

    number2 = 0
    operation = 0
    i = 0
    j = 0
    while i < N and j < N:
        number2 += mat[i][j]
        if operation % 2 == 0:
            i = i+1
        else:
            j = j+1
        operation += 1

    if number1 % 2 == K or number2 % 2 == K:
        print("YES")
    else:
        print("NO")
