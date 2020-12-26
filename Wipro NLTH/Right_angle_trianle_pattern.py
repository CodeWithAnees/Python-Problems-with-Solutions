# Right angle triangle pattern
# Write a program to print the right angle triangle pattern using * symbol.

# Input Format:

# Input consist of 1 integer

# Output Format:

# Refer sample output

# Sample Input:

# 5

# Sample Output:

# *   

# *   *   

# *   *   *  

# *   *   *   * 

# *   *   *   *  *

n = int(input())
for i in range(1,n+1):
    for j in range(i):
        print("*", end=" ")
    print()