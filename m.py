N = int(input())
A = []
even = []
odd = []
for i in input().split(" "):
    A.append(int(i))
    if int(i) % 2 == 0:
        even.append(int(i))
    else:
        odd.append(int(i))
if len(odd) >= len(even):
    print((len(odd)-len(even))/2)
else:
    m = 0
    for i in even:
        if len(even) == len(odd):
            break
        i /= 2
        if i % 2 != 0:
            even.remove(int(2*i))
            odd.append(int(i))
            m += 1
    if len(even) != len(odd):
        for i in even:
            if len(even) == len(odd):
                break
            i /= 4
            if i % 2 != 0:
                even.remove(int(4*i))
                odd.append(int(i))
                m += 1

    print(m)
