# Description
# 输入一个数组和一个数字，在数组中查找两个数，使得它们的和正好是输入的那个数字，统计这样两个数的对数。
#
# Input
# 输入第一行是数组，每一个数用空格隔开；第二行是数字和。
#
# Output
# 输出这样两个数有几对。
#
# Sample Input 1
# 1 2 4 7 11 0 9 15
# 11
#
# Sample Output 1
# 3

input_arr = input().split()
num = int(input())

count = 0
for i in range(len(input_arr)-1):
    for j in range(i+1, len(input_arr)):
        if int(input_arr[i]) + int(input_arr[j]) == num:
            count += 1
        else:
            continue
print(count)
