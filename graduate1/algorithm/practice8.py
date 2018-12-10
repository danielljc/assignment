if __name__ == "__main__":
    num = input()
    for i in range(int(num)):
        line = input().split()
        first = int(line.pop(0))
        sum = 0
        while len(line) > 0:
            sum += int(line.pop())
        print(sum)
        print('\n', end='')
