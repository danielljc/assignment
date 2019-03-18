# -*- coding: utf-8 -*-

# @Time   : 2019-03-18 21:03
# @Author : Daniel
# @Desc   : 硬币最小数量：给出不同面值硬币的清单和货币总额，输出组成该数量所需的最小硬币数量。
#           如果这些钱不能用给定的硬币补足，则输出-1。你可以假设每种类型的硬币数量都是无限的。
#           3 11 / 1 2 5 ==> 3


def change(money, coins):
    count = 0
    for i in range(len(coins)-1, -1, -1):
        count += money // int(coins[i])
        money = money % int(coins[i])

    if money == 0:
        return count
    else:
        return -1


if __name__ == '__main__':
    t = int(input())

    output = []
    for i in range(t):
        first_line = input().split()
        num = int(first_line[0])
        total = int(first_line[1])
        # 不同面额的硬币
        array = input().split()
        output.append(change(total, array))

    for i in range(len(output)):
        print(output[i])
