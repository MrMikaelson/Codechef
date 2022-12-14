# cook your dish here
L,R = input().split(" ")
L = int(L)
R = int(R)
if L%2!=0:
    start = L
else:
    start = L+1 
while start<=R:
    print(start,end=" ")
    start+=2