# cook your dish here
T = int(input())
for _ in range(T):
    Pa, Pb, Qa, Qb = input().split(" ")
    Pa = int(Pa)
    Pb = int(Pb)
    Qa = int(Qa)
    Qb = int(Qb)
    if Pa > Pb:
        P = Pa
    else:
        P = Pb
    if Qa > Qb:
        Q = Qa
    else:
        Q = Qb
    if P > Q:
        print("Q")
    elif P < Q:
        print("P")
    else:
        print("TIE")
