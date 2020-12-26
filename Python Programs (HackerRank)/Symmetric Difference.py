int(input())
set1 = set(map(int, input().split()))
int(input())
set2 = set(map(int, input().split()))
sdif = set1.symmetric_difference(set2)
sorted_sdif = sorted(sdif)
for i in sorted_sdif:
    print(i)
