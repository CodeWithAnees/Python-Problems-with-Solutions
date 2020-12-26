from collections import Counter

no_of_shoes = int(input())

av_sizes = Counter(map(int, input().split()))
sells = []
for i in range(int(input())):
    size, prize = map(int, input().split())
    if av_sizes[size]:
        sells.append(prize)
        av_sizes[size] -= 1

print(sum(sells))
# av_sizes = Counter(['2', '3', '4', '5', '6', '8', '7', '6', '5', '18'])
# print(av_sizes)
# print(av_sizes[5])
# b = []

# print(sizes)
