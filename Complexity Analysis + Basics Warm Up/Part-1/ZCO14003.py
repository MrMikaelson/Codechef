# cook your dish here
N = int(input())
customer = []
for i in range(N):
    customer.append(int(input()))
customer.sort()
revenue = []
for i in range(len(customer)):
    rev = (N-i)*customer[i]
    revenue.append(rev)
print(max(revenue))