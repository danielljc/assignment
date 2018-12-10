import sys
import time


def quick_sort_standard(array, low, high):
    if low < high:
        key_index = partition(array, low, high)
        quick_sort_standard(array, low, key_index)
        quick_sort_standard(array, key_index + 1, high)


def partition(array, low, high):
    key = array[low]
    while low < high:
        while low < high and array[high] <= key:
            high -= 1
        if low < high:
            array[low] = array[high]

        while low < high and array[low] > key:
            low += 1
        if low < high:
            array[high] = array[low]

    array[low] = key
    return low


sys.setrecursionlimit(1000000)
print("请输入测试文件的路径：")
path = sys.stdin.readline().strip()

# 读文件
file = open(path, 'r')
k = int(file.readline())
print("Top " + str(k) + " 为：", end="")
lines = file.readlines()
file.close()

temp = []
# 输出
output = []
start = time.time()
for line in lines:
    try:
        line = float(line.strip())
    except:
        print(line + "is not a correct data")
        continue
        # 加入数组
    temp.append(line)
quick_sort_standard(temp, 0, len(temp) - 1)

end = time.time()
print(",".join(str(key) for key in temp[0:k]))
# print("耗时为：" + str(end - start) + "秒")
