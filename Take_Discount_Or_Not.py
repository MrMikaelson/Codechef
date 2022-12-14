# cook your dish here
T = int(input())
for _ in range(T):
    N,X,Y = input().split(" ")
    N = int(N)
    X = int(X)
    Y = int(Y)
    total = 0
    A = input().split(" ")
    without_coupon = 0
    for i in A:
        i = int(i)
        if i<Y:
            without_coupon+=i
        else:
            without_coupon+=i
            total = total + i - Y
    with_coupon = X + total
    if with_coupon<without_coupon:
        print("COUPON")
    else:
        print("NO COUPON")