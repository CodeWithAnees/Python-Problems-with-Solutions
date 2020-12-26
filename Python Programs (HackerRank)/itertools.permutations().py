from itertools import permutations
a, b = input().upper().split()
for p in sorted(list(permutations(a,int(b)))):
    print(*p,sep="")
