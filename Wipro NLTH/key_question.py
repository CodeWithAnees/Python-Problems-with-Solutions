# Key Question
# Mr. Jason has captured your friend and has put a collar around his neck. He has locked it with a given ‘locking key’. It can be opened now with an ‘unlocking key’. Your friend has seen the ‘locking key’ but he does not know about the ‘unlocking key’. Given the locking key, one can figure out the ‘Unlocking key’ which is the smallest (in magnitude) permutation of the digits of that number. Help your friend to write an algorithm that takes the locking key as an input and outputs the unlocking key.

# Input Format:

#  The input consists of an integer K, representing the locking key.

# Output Format:

#  Print an integer representing the unlocking key

# Sample Input:

# 11

# Sample Output:

# 1 1

fkey = str(input())
l = list()
for i in fkey:
    l.append(i)

l.sort()

print(" ".join(l))
