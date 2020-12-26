l = list([])
for _ in range(int(input())):
    int(input())
    set_elements1 = set(map(int, input().split()))
    int(input())
    set_elements2 = set(map(int, input().split()))
    l.append(set_elements1.issubset(set_elements2))

for _ in l:
    print(_)
