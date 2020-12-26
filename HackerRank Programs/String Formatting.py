def print_formatted(number):
    width = len(bin(number).replace('0b', ""))+1
    for i in range(1, number + 1):
        print('{}{}{}{}'.format(str(i).rjust(width-1), oct(i).replace('0o', "").rjust(width), hex(i).replace('0x', "").upper().rjust(width), bin(i).replace('0b', "").rjust(width)))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)