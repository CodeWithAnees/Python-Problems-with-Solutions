if __name__ == '__main__':
    lis = []
    mar = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lis = lis + [[name, score]]
        mar += [score]
    second = sorted(set(mar))[1]

    for a, b in sorted(lis):
        if b == second:
            print(a)