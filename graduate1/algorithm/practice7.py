import sys

if __name__ == "__main__":
    try:
        while True:
            a, b = input().split()
            print(int(a)+int(b))
            print("\n", end="")
    except EOFError:
        sys.exit()
