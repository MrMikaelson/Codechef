# cook your dish here
from math import ceil


for _ in range(int(input())):
    N, X = input().split(" ")
    N = int(N)
    X = int(X)
    if X > (3*N) or X < -N:
        print("NO")
    else:
        if X < 0:
            print("YES")
            print(f"{0} {-X} {0}")
        else:
            a = ceil(X//3)
            # print(a)
            left = X - (3*a)
            # print(left)
            minimum_correct = a
            questions_left = N - minimum_correct
            # print(questions_left)
            if left == 0:
                print("Yes")
                A = a
                B = 0
                C = questions_left
                print(f"{A} {B} {C}")
            else:
                if questions_left == 0:
                    print("NO")
                else:
                    if left == 1 and questions_left >= 3:
                        print("YES")
                        A = a+1
                        B = 2
                        C = questions_left-3
                        print(f"{A} {B} {C}")
                    elif left == 2 and questions_left >= 2:
                        print("YES")
                        A = a+1
                        B = 1
                        C = questions_left-2
                        print(f"{A} {B} {C}")
                    else:
                        print("NO")
