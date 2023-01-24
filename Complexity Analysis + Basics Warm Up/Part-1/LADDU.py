# cook your dish here
for _ in range(int(input())):
    laddus = 0
    numOfActivities, origin = input().split(" ")
    if origin == 'INDIAN':
        redeem = 200
    else:
        redeem = 400
    for _ in range(int(numOfActivities)):
        activity_num = input().split(" ")
        if len(activity_num) > 1:
            if activity_num[0] == 'CONTEST_WON':
                laddus += 300
                if int(activity_num[1]) <= 20:
                    laddus += (20-int(activity_num[1]))
            else:
                laddus += int(activity_num[1])
        else:
            if activity_num == 'TOP_CONTRIBUTOR':
                laddus += 300
            else:
                laddus += 50
    print(laddus//redeem)