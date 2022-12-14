T = int(input())
for _ in range(T):
    N, K = input().split(" ")
    N = int(N)
    K = int(K)


    def number_of_non_zeros(a):
        zeros = 0
        for i in a:
            if i != 0:
                zeros += 1
        return zeros


    def last_number(a):
        for i in a:
            if i != 0:
                return i


    a = []
    for i in range(N):
        a.append(i+1)

    i = 0
    while number_of_non_zeros(a) > 1:
        a[i] = 0
        i = (i+K) % N

    number = last_number(a)

    if number%2==0:
        print("EVEN")
    else:
        print("ODD")