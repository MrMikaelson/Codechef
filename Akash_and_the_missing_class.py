for _ in range(int(input())):
    N = int(input())
    weeks = N//7
    leaves = weeks
    # print(weeks)
    remaining_days = N % 7
    # print(remaining_days)
    if remaining_days > 5:
        leaves += 1
    print(leaves)
