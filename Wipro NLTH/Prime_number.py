# Prime number
# A prime number is divisible only by 1 and itself. You are given a positive integer. Write an algorithm to find all the prime numbers from 2 to the given positive number.

# Input Format:

# The input consists of an integer num, representing the number written on the board.

# Output Format:

# Print space-separated integers representing the numbers required by the teacher.

# Constraints:

# 1 < num < 109

# Sample Input:

# 11

# Sample Output:

# 2 3 5 7

# Explanation:

# For the given number the list of special numbers is [2, 3, 5, 7, 11]

n = int(input())
prime_numbers = list()
for num in range(2, n):
    for i in range(2, num):
        if num%i == 0:
            break
    else:
        prime_numbers.append(num)

print(*prime_numbers)
