# cook your dish here
N = int(input())
for i in range(N):
    if i%2==0:
        for j in range(5*i+1,5*(i+1)+1):
                print(j,end=" ")
        print("\n")
    else:
        for j in range(5*(i+1),5*i,-1):
                print(j,end=" ")
        print("\n")