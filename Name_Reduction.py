# cook your dish here
def check(A, B):
    for i in A:
        if i in B:
            continue
        else:
            return False
    return True


def check_letter(a, A, B):
    if A.count(a) == B.count(B):
        return True
    else:
        return False


T = int(input())
for i in range(T):
    A, B = input().split(" ")
    AB = []
    for i in A+B:
        AB.append(i)
    N = int(input())
    ans = []
    for i in range(N):
        C = input()
        for i in C:
            if not check_letter(i, C, AB):
                print("NO")
        ans.append(check(C, AB))
    if False in ans:
        print("NO")
    else:
        print("YES")
