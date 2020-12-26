int(input())
set1 = set(map(int, input().split()))
int(input())
set2 = set(map(int, input().split()))
set3 = set1|set2
print(len(set3))