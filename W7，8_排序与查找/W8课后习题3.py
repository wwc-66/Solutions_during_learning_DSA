'''
3:散列表
查看提交统计提问
总时间限制: 500ms 内存限制: 65536kB
描述
给定一个指定大小N的散列表，并输入一系列数字：若找到空槽，则插入该数字，并返回槽位置；若该数字在散列表中存在，则直接输出其位置。

注：使用下标增加的二次探测法解决散列冲突

注2：散列表实际大小应确定为不小于用户输入N的最小质数



参考代码模板：

def createHashTable(n):
    # code here
    pass

def insertNumbers(table, nums):
    # code here
    pass

n = int(input())
nums = list(map(int, input().split()))
table = createHashTable(n)
insertNumbers(table, nums)

输入
两行

第一行为用户指定散列表大小整数N

第二行为一系列数字，以空格分隔
输出
逐个输出对应数字在散列表中位置，以空格分隔

若该数字无法插入，则输出“-”
样例输入
4

10 6 4 10 15
样例输出
0 1 4 0 -
'''