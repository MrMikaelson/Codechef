# cook your dish here
for _ in range(int(input())):
    N = int(input())
    speeds = list(map(int, input().split()))
    maxSpeed = speeds[0]
    maxCars = 0
    for i in speeds:
        if i <= maxSpeed:
            maxCars += 1
            maxSpeed = i
    print(maxCars)