import sys

# 题目：子矩阵问题
#
# Description
# 给定一个矩形区域，每一个位置上都是1或0，求该矩阵中每一个位置上都是1的最大子矩形区域中的1的个数。
#
# Input
# 输入的每一行是用空格隔开的0或1。
#
# Output
# 输出一个数值。
#
# Sample Input 1
# 1 0 1 1
# 1 1 1 1
# 1 1 1 0
#
# Sample Output 1
# 6


def largest_rectangle_area(heights):
    max_area = 0
    if not heights:
        return max_area
    heights.append(0)
    stack = [heights[0]]
    # 从数组的第二个元素开始遍历
    for arr_index in range(1, len(heights)):
        # 倒序遍历栈
        for stack_index in range(len(stack) - 1, -1, -1):
            # 若数组的当前的元素小于栈顶元素
            if heights[arr_index] < stack[stack_index]:
                top = stack.pop()
                # 计算面积：栈顶元素 * 次序
                area = top * (arr_index - len(stack))
                # 取面积较大值
                max_area = max(max_area, area)
            else:
                break
        # 若stack的栈顶指针小于arr的指针
        if len(stack) - 1 < arr_index:
            # 将pop出来的元素都用arr当前所指向的元素来填满，并把该元素放入栈内
            for j in range(arr_index - len(stack) + 1):
                stack.append(heights[arr_index])
    return max_area


def others_largest_rectangle_area(self, height):
    res = 0
    if not height:
        return res
    stack = []
    height.append(-1)
    for i in range(len(height)):
        current = height[i]
        while len(stack) != 0 and current <= height[stack[-1]]:
            h = height[stack.pop()]
            w = i if len(stack) == 0 else i - stack[-1] - 1
            res = max(res, h * w)
        stack.append(i)
    return res


def maximal_rectangle(matrix):
    res = 0
    if not matrix:
        return res
    # 初始化height = [0, 0 ,0 ....]
    height = [0 for i in range(len(matrix[0]))]
    for row in matrix:
        # 以第i行为x轴
        for i in range(len(row)):
            # 若为0，则从头开始计数
            if row[i] == '0':
                height[i] = 0
            else:
                height[i] += 1
        res = max(res, largest_rectangle_area(height))
    return res


# 当没有接受到输入结束信号就一直遍历每一行，按下换行键然后Ctrl+d结束
matrix = []
maximum = 0
for line in sys.stdin:
    input_arr = line.split()
    matrix.append(input_arr)
print(maximal_rectangle(matrix))
