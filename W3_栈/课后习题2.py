'''
2:一维开心消消乐
总时间限制: 1000ms 内存限制: 65536kB
描述
题目内容：

开心消消乐我们都熟悉，我们可以用刚学过的栈来做一个“一维”的开心消消乐游戏，这个游戏输入一串字符，逐个消去相邻的相同字符对。

如果字符全部被消完，则输出不带引号的“None”


输入格式:

一个字符串，可能带有相邻的相同字符，如“aabbbc”


输出格式：

一个字符串，消去了相邻的成对字符，如“bc”


输入样例1：

beepooxxxyz

输出样例1：

bpxyz


输入样例2：

kxkx

输出样例2：

kxkx


输入样例3：（这里bb被消了以后，第二个a挨上来了，所以两个a也相邻，同样消去）

abbacddccc00

输出样例3：

None



输入
一个字符串，可能带有相邻的相同字符，如“aabbbc”
输出
一个字符串，消去了相邻的成对字符，如“bc”
样例输入
beepooxxxyz
样例输出
bpxyz
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

def match_game(n):
    s = Stack()
    for char in n:
        if not s.isEmpty() and s.peek() == char:
            s.pop()
        else:
            s.push(char)

    if s.isEmpty():
        return 'None'
    else:
        return ''.join(s.items)

n1 = str(input())
print(match_game(n1))