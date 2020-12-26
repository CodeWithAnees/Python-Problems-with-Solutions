# Alphabetic cross pattern
# Write a program to print the following pattern.

# Input Format:

# Input consists of a string.

# Output Format:

# Refer sample output.

# Sample Input:

# hello

# Sample Output:

# h      o

#  e   l

#    l

#  e   l

# h      o 

word = input()
lengthOfWord = len(word)

for i in range(lengthOfWord):
    j = (lengthOfWord-1)-i
    for k in range(lengthOfWord):
        if(k==i or k==j):
            print(word[k],end="")
        else:
            print(end=" ")
    print("")

