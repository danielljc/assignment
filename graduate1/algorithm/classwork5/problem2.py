# -*- coding: utf-8 -*-

# @Time   : 2019-03-18 21:03
# @Author : Daniel
# @Desc   : 时间分隔：给定到达火车站的所有列车的到站和发车时间。你的任务是找到火车站所需要的最低站台数量，这样就不会有火车等待了。
#           900  940 950  1100 1500 1800
#           910 1200 1120 1130 1900 2000    ==> 3


def platform(arrive, depart):
    if len(arrive) == 0:
        return 0

    count = 1
    plat = [int(depart[0])]
    for i in range(1, len(arrive)):
        flag = 1
        for j in range(len(plat)):
            if int(arrive[i]) > int(plat[j]):
                plat[j] = depart[i]
                flag = 0
                break
            else:
                continue
        if flag == 1:
            plat.append(depart[i])
        count += flag
    return count

if __name__ == '__main__':
    t = int(input())

    output = []
    for i in range(t):
        num = int(input())
        arrive = input().split()
        depart = input().split()
        output.append(platform(arrive, depart))

    for i in range(len(output)):
        print(output[i])
