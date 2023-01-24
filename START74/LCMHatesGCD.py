# cook your dish here
def compute_gcd(x, y):

   while(y):
       x, y = y, x % y
   return x

# This function computes LCM
def compute_lcm(x, y):
   lcm = (x*y)//compute_gcd(x,y)
   return lcm

for _ in range(int(input())):
    A,B = map(int,input().split())
    if B%A == 0:
        print(0)
    else:
        X = compute_gcd(A,B)
        print(compute_lcm(A,X) - compute_gcd(B,X))
    