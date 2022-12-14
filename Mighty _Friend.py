import itertools
list1 = []


subs = list(itertools.combinations(list1, 2))
if len(list1) % 2 == 0:
    for i in subs:
        for j in subs:
            if i != j:
                continue
            else:
                if sum(i) == sum(j):
                    print(True)
