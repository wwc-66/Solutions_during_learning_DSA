'''
3:基数排序
总时间限制: 500ms 内存限制: 65536kB
描述
实现一个基数排序算法，用于10进制的正整数从小到大的排序。

思路是保持10个队列(队列0、队列1......队列9、队列main)，开始，所有的数都在main队列，没有排序。

第一趟将所有的数根据其10进制个位(0~9)，放入相应的队列0~9，全放好后，按照FIFO的顺序，将每个队列的数合并排到main队列。

第二趟再从main队列队首取数，根据其十位的数值，放入相应队列0~9，全放好后，仍然按照FIFO的顺序，将每个队列的数合并排到main队列。

第三趟放百位，再合并；第四趟放千位，再合并。

直到最多的位数放完，合并完，这样main队列里就是排好序的数列了。


代码模板(建议复制粘贴使用)：

def func(mylist):
    # your code here
    return output

mylist = eval(input())
print(func(mylist))


输入
一个列表mylist，其中mylist包含一些需要排序的正整数，正整数互不相同且均不超过100000，且个数在1至1000之间。
输出
一个与mylist等长的列表。
样例输入
[8, 91, 34, 22, 65, 30, 4, 55, 18]
样例输出
[4, 8, 18, 22, 30, 34, 55, 65, 91]
'''
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def __str__(self):
        return ''.join(self.items)


def func(mylist):
    if not mylist:
        return []
    # 创建十个用于匹配并存放数字的队列和一个最终返回的排序完成的队列
    queues = [[] for _ in range(10)]
    main_queue = mylist.copy()

    # 找出最大数字并确定所需要排序的次数
    max_num = max(mylist)
    max_digits = len(str(max_num))

    # 从个位数开始依次执行排序
    for i in range(max_digits):
        # 将每轮被排序的数字存入对应的队列
        while main_queue:
            num = main_queue.pop(0)
            # 获取当前位数的数字并存入
            digit = (num // (10 ** i)) % 10
            queues[digit].append(num)

        # 经过排序后的数字返回主队列
        for j in range(10):
            while queues[j]:
                main_queue.append(queues[j].pop(0))
    return main_queue


mylist = eval(input())
print(func(mylist))