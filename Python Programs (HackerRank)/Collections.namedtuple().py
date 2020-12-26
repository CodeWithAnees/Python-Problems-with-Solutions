from collections import namedtuple

n, titles = int(input()), input().split()
table = namedtuple('titles', titles)
marks = [int(table._make(input().split()).MARKS) for _ in range(n)]
print("{0:.2f}".format(sum(marks) / len(marks)))
