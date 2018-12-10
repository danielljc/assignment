import sys

if __name__ == "__main__":
    list_line = []
    results = []
    for in_line in sys.stdin:  # 当没有接受到输入结束信号就一直遍历每一行，按下换行键然后Ctrl+d结束
        line = in_line.split()  # 对字符串利用空字符进行切片
        list_line.append(line)  # 把每行的字符串合成到列表
        if line:
            first = int(line[0])
            list_sum = 0
            if first == 0:
                result = list_sum
            else:
                # 若N大于实际数组的长度，则取实际长度；若N小于实际数组的长度，则依然取N的长度
                minimum = first if (len(line) - 1) >= first else len(line) - 1
                for i in range(1, minimum + 1):
                    list_sum += int(line[i])
                result = list_sum
            results.append(result)

    # 换行输出
    for result in results:
        print(result)
