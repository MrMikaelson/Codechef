# cook your dish here
T = int(input())
for _ in range(T):
    X, Y = input().split(" ")
    X = int(X)
    Y = int(Y)
    diff = X-Y
    if diff > 0:
        if diff % 2 == 0:
            operations = diff//2
        else:
            operations = diff//2
            operations+=2
    else:
        diff = Y-X
        operations = diff
    print(operations)
