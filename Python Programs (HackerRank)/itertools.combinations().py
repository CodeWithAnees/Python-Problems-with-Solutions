from itertools import combinations

word, length = input().split()
b = list()
for i in range(1, int(length) + 1):
    l = sorted(list(combinations(sorted(word.upper()), i)))
    b.append(l)

for i in b:
    for j in i:
        print(*j, sep="")
