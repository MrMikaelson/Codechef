# cook your dish here
N = int(input())
for _ in range(N):
    string = input()
    lengthOfString = len(string)
    if lengthOfString%2==0:
        firstHalf = string[:(lengthOfString//2)]
        firstHalf = list(firstHalf)
        firstHalf.sort()
        secondHalf = string[lengthOfString//2:]
        secondHalf = list(secondHalf)
        secondHalf.sort()
        if firstHalf == secondHalf:
            print("YES")
        else:
            print("NO")
    else:
        firstHalf = string[:(lengthOfString//2)]
        firstHalf = list(firstHalf)
        firstHalf.sort()
        secondHalf = string[lengthOfString//2+1:]
        secondHalf = list(secondHalf)
        secondHalf.sort()
        if firstHalf == secondHalf:
            print("YES")
        else:
            print("NO")