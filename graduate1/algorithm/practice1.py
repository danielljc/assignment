import sys

if __name__ == "__main__":
    try:
        while True:
            a, b = map(int, input().split())
            print(a+b)
    except EOFError:
        sys.exit()