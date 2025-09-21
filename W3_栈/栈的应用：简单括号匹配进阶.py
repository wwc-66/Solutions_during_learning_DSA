'''
问题进阶：
假如匹配括号的种类由单一的小括号一种，
增加中括号和大括号，
又该怎么编写程序来实现匹配的功能？
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
    match_table = {')':'(',']':'[','}':'{'}
    matched = True
    for char in n:
        if char in match_table.values():
            s.push(char)
        else:
            if s.peek() != match_table[char]:
                matched = False
            else:
                s.pop()

    if matched and s.isEmpty():
        return True
    else:
        return False

n1 = str(input())
print(parCheck(n1))

'''
上述代码为本人初代编写代码，存在以下问题：
1.假设栈为空时，检测到了闭括号，peek会导致程序报错
2.matched不必单独设立，移除此变量，直接返回结果，简化逻辑

解决方案：
1.当检测到的括号为闭括号时，在前方设置一层检测栈是否为空的条件，如果检测为空，直接return false
2.移除matched变量，直接返回结果

修改完善代码(很巧，这也是课后习题1的答案)：
def parCheck(n):
    s = Stack()
    match_table = {')':'(',']':'[','}':'{'}
    
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
'''