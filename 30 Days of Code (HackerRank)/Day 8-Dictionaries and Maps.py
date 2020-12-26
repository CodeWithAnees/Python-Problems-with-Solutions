phonebook = {}
entries = int(input())

for n in range(entries):
    name, num = input().strip().split(' ')
    name, num = [str(name), int(num)]
    phonebook[name] = num

while True:
    try:
        search = str(input())

        if search in phonebook:
            output = ''.join('%s=%r' % (search, phonebook[search]))
            print(output)
        else:
            print("Not found")
    except EOFError:
        break





# z = int(input())
#
# d = {}
# for i in range(z):
#     name, phone = input().split()
#     d[name] = phone
#
# # print(d)
# # print(d.keys())
# for j in range(z):
#     want = input()
#     if want in d.keys():
#         print("{}={}".format(want,d[want]))
#     else:
#         print("Not found")
#
#     # for k in d.keys():
#     #     print(k)
#         # if want == k:
#         #     print(k,end=" = ")
#         #     print(d[k])
#         # else:
#         #     print("Not found")
