T=int(input())
for i in range(T):
    n=int(input())
    a=0 
    b=5 
    while(n//b)>0:
        a+=n//b
        b*=5
    print(a)