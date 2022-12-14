# cook your dish here
a,b,c = map(int, input().split())
def triangle(a,b,c):
    if a+b>c and b+c>a and a+c>b:
        
        if a==b and b==c and c==a:
            return 1 
        if a==b or b==c or a==c:
            return 2
        if a!=b and b!=c and a!=c:
            return 3
    else:
        return -1
        
print(triangle(a,b,c))