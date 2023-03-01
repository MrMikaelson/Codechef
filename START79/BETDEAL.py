import math
# cook your dish here
for _ in range(int(input())):
    first_D,second_D = input().split()
    first_price = 100*(1-(int(first_D)/100))
    secondPrice = 200*(1-(int(second_D)/100))
    if first_price % 1 < 0.5:
        first_price = math.floor(first_price)
    if first_price%1 > 0.5:
        first_price = math.ceil(first_price)
    if secondPrice%1 < 0.5:
        secondPrice = math.floor(secondPrice)
    if secondPrice%1 > 0.5:
        secondPrice = math.ceil(secondPrice)
    if first_price < secondPrice:
        print("FIRST")
    elif first_price > secondPrice:
        print("SECOND")
    else:
        print("BOTH")