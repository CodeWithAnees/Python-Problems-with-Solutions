n, m = list(map(int, input().split()))
given_numbers = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
total = 0
for i in given_numbers:
    if i in A:
        total += 1
    elif i in B:
        total -= 1
print(total)

# Another solution:
# print(sum([(i in A) - (i in B) for i in given_numbers]))

# Rules need to know: True = 1 and False = 0
# True - False    = 1
# True - True     = 0
# False - True    = -1
# False - False   = 0
