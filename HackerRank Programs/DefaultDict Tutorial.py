from collections import defaultdict

dlist = defaultdict(list)
mlist = []

n, m = map(int, input().split())

for i in range(0, n):
    dlist[input()].append(i + 1)

for i in range(0, m):
    mlist.append(input())

for i in mlist:
    if i in dlist:
        print(" ".join(map(str, dlist[i])))
    else:
        print(-1)
