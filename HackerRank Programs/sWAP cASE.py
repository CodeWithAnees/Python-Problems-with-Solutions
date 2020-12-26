def swap_case(s):
    result = ''
    a = list(s)
    for i in a:
        if i==i.lower():
            up = i.upper()
            result += up

        elif i==i.upper():
            low = i.lower()
            result += low
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)