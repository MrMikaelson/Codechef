# cook your dish here
a,b,c = map(int,input().split())
if a>0 and b>0 and c>0 and a+b+c == 180:
    print("YES")
else:
    print("NO")