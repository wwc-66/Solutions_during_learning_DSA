'''
3:强迫症老板和他的洗碗工
总时间限制: 1000ms 内存限制: 65536kB
描述
题目内容：

洗碗工小明碰上了一位强迫症老板老王，餐厅一共就10只盘子，老板给仔细编上了0～9等10个号码，并要求小明按照从0到9的编号来洗盘子，当然，每洗好一只盘子，就必须得整齐叠放起来。


小明洗盘子期间，经常就有顾客来取盘子，当然每位顾客只能从盘子堆最上面取1只盘子离开。


老王在收银台仔细地记录了顾客依次取到盘子的编号，比如“1043257689”，这样他就能判断小明是不是遵照命令按照0123456789的次序来洗盘子了。


你也能像老王一样作出准确的判断吗？

输入
长度为10的字符串，其中只包含0～9的数字，且不重复，代表顾客依次取到的盘子编号
输出
字符串：Yes或者No，表示遵照次序洗盘子，或者没有遵照次序洗盘子
样例输入
1043257689
样例输出
Yes
'''

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

s = Stack()
dishes = input()
index = 0
for i in range(0,10):
#依次洗盘并存放
    s.push(str(i))
    while not s.isEmpty() and index < len(dishes) and s.peek() == dishes[index]:
    #一旦放置好的盘子编号与输入字符串中正在受检测的盘子编号匹配，则pop此盘子，同时继续排查是否存在连续取盘
        s.pop()
        index += 1

if s.isEmpty():
#洗盘取盘成功一一对应
    print('Yes')
else:
    print('No')