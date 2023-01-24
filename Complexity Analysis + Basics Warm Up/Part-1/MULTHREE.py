# cook your dish here
for _ in range(int(input())):
    a,b,c=map(int,input().split())
    s1,s2=b+c,b+c
    if (b+c)%2==1 and a>2:
        s2+=(s2%10)
        a-=1 
    #print(a)
    for i in range((a-2)%12):
        s2+=(s2%10) 
        #print(s2)
    if s2%3==0:
        print("YES")
    else:
        print("NO")