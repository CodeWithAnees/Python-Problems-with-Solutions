from collections import Counter
size= int(input())
l = list(input().split())
rooms = Counter(l)
for key, value in rooms.items():
    if value == 1:
        print(key)
        break










# size_of_group = int(input())
# family = sorted(list(map(int, input().split())))
# print(family)
# for i in family[0::size_of_group]:
#     print(i)










# print(family)

