'''
1:有效的括号
总时间限制: 1000ms 内存限制: 65536kB
描述
题目内容：

给定一个只包括 '('，')'，'{'，'}'，'['，']'
的字符串，判断字符串是否有效。


有效字符串需满足：

左括号必须用相同类型的右括号闭合。

左括号必须以正确的顺序闭合。

注意空字符串可被认为是有效字符串。


输入格式:

一行字符串


输出格式：

True或False，表示该输入是否为合法括号串


输入样例1：

([])


输出样例1：

True



输入样例2：

{{)]}


输出样例2：

False




输入
一行字符串
输出
True或False，表示该输入是否为合法括号串
样例输入
([])
样例输出
True
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

def parCheck(n):
    s = Stack()
    match_table = {')': '(', ']': '[', '}': '{'}

    for char in n:
        if char in match_table.values():  # 开括号
            s.push(char)
        elif char in match_table:  # 闭括号
            if s.isEmpty():
                return False  # 栈为空但遇到闭括号，不匹配
            if s.peek() == match_table[char]:
                s.pop()  # 匹配成功，弹出栈顶元素
            else:
                return False  # 类型不匹配

    return s.isEmpty()  # 栈为空表示所有括号都匹配

n1 = str(input())
print(parCheck(n1))