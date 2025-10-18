'''
2:最近的请求次数
总时间限制: 500ms 内存限制: 65536kB
描述
计算每个事件发生之时，往前算10000毫秒内有多少个事件发生，包含当事件；也即对于列表中的每个元素k，算出整个列表中有多少个元素介于k-10000和k（两端均含）之间。

代码模板(建议复制粘贴使用)：

def func(mylist):
    # your code here
    return output

mylist = eval(input())
print(func(mylist))

输入
一个已排序列表mylist，所有元素为非负整数，记录各个请求的发生时间，单位为毫秒。
输出
一个与mylist等长的列表。
样例输入
[0,10,100,1000,10000,20000,100000]
样例输出
[1, 2, 3, 4, 5, 2, 1]
'''

def func(mylist):
    output = []
    for i in range(0, len(mylist)):#进行计算操作的次数，同时也保证了返回列表的长度与输入列表相同
        count = 0
        for item in mylist:
            if (item >= mylist[i]-10000) and item <= mylist[i]:
                count += 1
        output.append(count)

    return output

mylist = eval(input())
print(func(mylist))
'''
本题答案在OJ提交答案后由于运行时长超过限制时长500ms，不予通过，后续将进行改善与更新
'''