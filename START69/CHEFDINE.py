# cook your dish here
T = int(input())
for _ in range(T):
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    categories = {}
    list_set = set(A)
    unique_list = (list(list_set))
    for i in unique_list:
        categories[i] = []
    for i in range(N):
        categories[A[i]].append(B[i])
        time = []
    for i in categories:
        time.append(min(categories[i]))
    # print(categories)
    time.sort()
    # print(time)
    if K > len(unique_list):
        print(-1)
        continue
    print(sum(time[:K]))
    
    
        