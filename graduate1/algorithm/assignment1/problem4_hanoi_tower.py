# 题目：汉诺塔
#
# Description
# 汉诺塔问题中限制不能将一层塔直接从最左侧移动到最右侧，也不能直接从最右侧移动到最左侧，而是必须经过中间。求当有N层塔的时候移动步数。
#
# Input
# 输入的第一行为N。
#
# Output
# 移动步数。

count = 0


# 将x的第一个元素移到y
def move(x, y):
    global count
    y.append(x.pop())
    count += 1


# 递归只要考虑初始情况与递归情况即可，拆分为1与n-1来看
def hanoi(n, a, b, c):
    global count
    # 初始条件
    if n == 1:
        move(a, b)
        move(b, c)
    else:
        # 通项公式
        hanoi(n-1, a, b, c)
        move(a, b)
        hanoi(n-1, c, b, a)
        move(b, c)
        hanoi(n-1, a, b, c)


if __name__ == '__main__':
    n = int(input())
    a = [n-i for i in range(n)]
    b = []
    c = []
    # move 1~n from a to c
    hanoi(n, a, b, c)
    print(count)
