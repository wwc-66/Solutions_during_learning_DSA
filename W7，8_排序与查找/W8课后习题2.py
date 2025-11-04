'''
2:列表出现最频繁的元素
总时间限制: 500ms 内存限制: 65536kB
描述
给定一个列表与数字K，按出现次数倒序输出列表中前K个出现最频繁的元素；若少于K个元素则返回所有元素。若有两个或以上的元素出现次数相等，按元素的值进行顺序输出，小的在前。

参考代码模板：

def topKFrequent(nums, k):
    # code here
    pass

lst = eval(input())
k = int(input())
topKFrequent(lst, k)

输入
输入为两行
第一行为给定列表，以合法的Python表达式给出
第二行为数字K
输出
不多于K个数字，以空格分隔
样例输入
[2,1,1,1,2,2,3]

2
样例输出
1 2
'''

def topKFrequent(nums, k):
    #如果数字数量少于k，输出所有元素
    if len(set(nums)) < k:
        return ' '.join(x for x in set(nums))
    #创建空字典，用于统计数字出现频率
    numbers = {}
    #遍历列表并计算出现次数
    for n in nums:
        if n not in numbers:
            numbers[n] = 1
        else:
            numbers[n] += 1

    #创建元组列表
    freq_lst = [(num,freq) for num, freq in numbers.items()]
    #对元组列表进行排序
    freq_lst.sort(key = lambda x: (-x[1],x[0]))
    #结果列表为排好序的k个元素
    result = [item[0] for item in freq_lst[:k]]
    return ' '.join(str(r) for r in result)



lst = eval(input())
k = int(input())
print(topKFrequent(lst, k))

'''提交结果运行时长超时，但功能正常实现'''