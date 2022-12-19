# cook your dish here
def subOr(list):
    sub = 0
    for i in list:
        sub = sub | i
    return sub 
def sub_lists (l):
    lists = [[]]
    for i in range(len(l) + 1):
        for j in range(i):
            lists.append(l[j: i])
    return lists
def notInSubArray(integers,subArray):
    return [x for x in integers if x not in subArray]
T = int(input())
for _ in range(T):
    N = int(input())
    integers = list(map(int,input().split()))
    subArray = sub_lists(integers)
    length = [-1]
    for i in subArray:
        notSubArray = notInSubArray(integers,i)
        if subOr(i) == subOr(notSubArray):
            length.append(len(i))
            
    print(max(length))
    
        
    
        