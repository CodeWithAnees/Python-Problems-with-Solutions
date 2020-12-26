import itertools

elements = input()
for key, group in itertools.groupby(elements):
    print((len(list(group)), int(key)), end=" ")

# Another Solution is:
# print(*[(len(list(c)), int(k)) for k, c in groupby(input())])


# print(l)
# print(keys)
# for i in group:
#     # print(len(i))
#     m.append(len(i))
#
#     # print()
# print(m)
#
# for i in keys:
#     for j in m:
#         print(i,j)
#
#
#
#
#
# # for i, j in keys,group:
# #     m.append(i,j)
# # print(m)
