# cook your dish here
for _ in range(int(input())):
    N = int(input())
    A = input().split()
    B = input().split()
    mostPopular = 0
    for i in range(N):
        if int(A[mostPopular]) < int(A[i]):
            mostPopular = i
        elif int(A[mostPopular]) == int(A[i]):
            if int(B[mostPopular]) < int(B[i]):
                mostPopular = i
    print(mostPopular+1)