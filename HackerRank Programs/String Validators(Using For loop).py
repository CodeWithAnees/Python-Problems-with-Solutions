if __name__ == '__main__':
    s = input()

for i in s:
    if i.isalnum() == True:
        ans = True
        break
    else:
        ans = False
print(ans)

for i in s:
    if i.isalpha() == True:
        ans = True
        break
    else:
        ans = False
print(ans)

for i in s:
    if i.isdigit() == True:
        ans = True
        break
    else:
        ans = False
print(ans)

for i in s:
    if i.islower() == True:
        ans = True
        break
    else:
        ans = False
print(ans)

for i in s:
    if i.isupper() == True:
        ans = True
        break
    else:
        ans = False
print(ans)