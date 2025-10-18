'''
1:有序队列
总时间限制: 500ms 内存限制: 32000kB
描述
一开始给出了一个由小写字母组成的字符串 S。我们规定每次移动中，选择最左侧的字母，将其从原位置移除，并加到字符串的末尾。这样的移动可以执行任意多次

返回我们移动之后可以拥有的最小字符串（注：在Python3中，字符串的大小可用不等号比较）。


代码模板(建议复制粘贴使用)：

def func(S):
    # your code here
    return output

S = eval(input())
print(func(S))

输入
S。S为仅含有小写字母的字符串，长度不超过100000。
输出
一个与S等长的字符串。
样例输入
"cba"
样例输出
acb
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

def func(se):
    s = Queue()
    for char in se:
        s.enqueue(char)#生成一个由输入字符se的字符依次组成的队列
    st = str(s)#将原队列设为初始被比较字符

    for i in range(s.size()):
        #进行与字符串等长次数的转换
        s.enqueue(s.dequeue())

        current = str(s)

        if current < st:
            #将本次得到的字符与上一次的较小字符比较，更小者成为新的被比较字符，直到得出最小的结果
            st = current

    return st

S = eval(input())
print(func(S))