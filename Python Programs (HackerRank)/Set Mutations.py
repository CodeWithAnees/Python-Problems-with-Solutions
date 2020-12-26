no_of_elements = int(input())
A = set(map(int, input().split()))
no_of_operations = int(input())
for i in range(0, no_of_operations):
    command, no_of_command = input().split()
    B = set(map(int, input().split()))
    if command == 'update':
        A.update(B)
    elif command == 'intersection_update':
        A.intersection_update(B)
    elif command == 'symmetric_difference_update':
        A.symmetric_difference_update(B)
    elif command == 'difference_update':
        A.difference_update(B)

print(sum(A))
