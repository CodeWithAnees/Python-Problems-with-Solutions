# Symbolic pattern 1
# Write a program to print the following pattern.

# Input Format:

# Input consists of a both number of rows and columns as a single input.

# Output Format:

# Refer the sample output.

# Sample Input:

# 5

# Sample Output:

#   *  
#   *  
# *****
#   *  
#   *

import math

n = int(input())

middle = math.ceil(n/2)
if n%2 == 0:
    middle = middle+1

for i in range(1,n):
    if i == middle:
        for z in range(n):
            print("*",end="")
        print("")
    for j in range(1,middle):
        print(" ",end="")
    print("*")