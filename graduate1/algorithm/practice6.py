if __name__ == "__main__":
    while True:
        line = input().split()
        if line:
            first = int(line[0])
            list_sum = 0
            if first == 0:
                print(list_sum)
            else:
                minimum = first if (len(line)-1) >= first else len(line)-1
                for i in range(1, minimum+1):
                    list_sum += int(line[i])
                print(list_sum)