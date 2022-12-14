for _ in int(input()):
    N, K = input().split(" ")
    N = int(N)
    K = int(K)
    if K == 1:
        if N%2==0:
            print("EVEN")
        else:
            print("ODD")
    elif K == 2:
        print("ODD")
    else:
        print("EVEN")
