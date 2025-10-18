'''
1:进制转换
总时间限制: 1000ms 内存限制: 65536kB
描述
题目内容：

给定一个M进制的数，请将其转换为N进制并输出

输入
两行，第一行为空格分隔的两个数字，分别为10进制表示的M与N；其中M, N均满足2 ≤ M、N ≤ 36

第二行为待转换的M进制数字，其中每位超过9的部分从10至36分别用大写字母A-Z表示；输入数据保证数据的每一位不超过M
输出
一行字符串，表示转换后的N进制数
样例输入
8 16
471
样例输出
139
'''

s = input().split(' ')
M = int(s[0])
N = int(s[1])
K = input()
conS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def transto10(k, m):
    num = 0
    for ch in k:
        num = num * m + conS.index(ch)
    return int(num)


def toStr(num, n):
    if num < n:
        return conS[num]

    else:
        return toStr(num // n, n) + conS[num % n]


print(toStr(transto10(K, M), N))