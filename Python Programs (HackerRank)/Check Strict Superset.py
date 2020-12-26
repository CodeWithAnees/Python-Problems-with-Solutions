superset = set(map(int, input().split()))
l = list()
for _ in range(int(input())):
    given_set = set(map(int, input().split()))
    if superset - given_set == set() or superset.issuperset(given_set) == False:
        l.append(False)
    else:
        l.append(True)
print(all(l))