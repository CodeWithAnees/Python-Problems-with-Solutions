from itertools import  combinations_with_replacement
word, size = input().upper().split()
w = sorted(word)
for i in list(combinations_with_replacement(w, int(size))):
    print(*i, sep="")
