# cook your dish here
def x(A):
    min_pos = float('inf')
    max_neg = float('-inf')
    for i in A:
        if int(i)>0:
            if min_pos > int(i):
                min_pos = int(i)
        elif int(i) < 0:
            if max_neg < int(i):
                max_neg = int(i) 
        else:
            print(-1)
            return
    if (min_pos - 1 )< (-max_neg):
        print(min_pos-1)
    else:
        print(-max_neg-1)
for _ in range(int(input())):
    N = int(input())
    A = input().split()
    x(A)