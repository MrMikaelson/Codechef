# cook your dish here
N,K=map(int,input().split())
numbers=list(map(int,input().split()))
numbers.sort()

def search(nums, target):
    start = 0
    end = len(nums)-1
    while start <= end:
        mid = start + (end-start)//2
        if int(nums[mid]) > target:
            end = mid-1
        elif int(nums[mid])< target:
            start = mid+1
        else:
            return 1
    return -1

print(search(numbers,K))