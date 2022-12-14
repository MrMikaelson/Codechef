# for _ in range(int(input())):
#     N = int(input())
#     distincts = 0
#     for i in range(N):
#         if (i+1) % 2 != 0:
#             distincts += 1
#     print(distincts)

from math import ceil


for _ in range(int(input())):
    N = int(input())
    distincts = ceil(N/2)
    print(distincts)
