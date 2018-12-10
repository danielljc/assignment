import sys

if __name__ == "__main__":
    while True:
        line = input().split()
        first = int(line.pop(0))
        if first == 0:
            sys.exit()
        else:
            sum = 0
            while len(line) > 0:
                sum += int(line.pop())
            print(sum)
