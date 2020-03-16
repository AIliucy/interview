# -*- coding: utf-8 -*-
"""
字符A-Z可以编码为0-25。"A"->"0", "B"->"1", ..., "Z"->"25"
现在输入一个数字序列，计算有多少种方式可以解码成字符A-Z组成的序列。
例如：
输入：19
输出：2
输入：258
输出：2
输入：0219
输出：3
"""


def how_many_ways(digitarray):

    digitarray = digitarray.lstrip('0')
    len_digitarray = len(digitarray)
    if len == 0:
        return 1
    li = list(range(len_digitarray+1))
    li[0] = 1
    for i in range(len_digitarray+1):
        if i == 0:
            continue
        elif digitarray[i-1] == '0':
            li[i] = 1
        else:
            li[i] = li[i-1]
        if (i > 1 and int(digitarray[i-1]) <= 6 and int(digitarray[i-2]) == 2) or (i > 1 and int(digitarray[i-2]) == 1):
            li[i] += li[i-2]

    return li[-1]


while True:
    digitarray = input('请输入要解码的数字序列：')
    result = how_many_ways(digitarray)
    print('解码结果为：%d' % result)
