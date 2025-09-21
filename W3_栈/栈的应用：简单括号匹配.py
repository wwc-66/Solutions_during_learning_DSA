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
    matched = True
    index = 0
    while index < len(n) and matched:
        symbol = n[index]
    #依次输入字符串的括号
        if symbol == '(':
            s.push(symbol)
            #如果输入的是左括号，将其放入栈中等待匹配
        else:
            #输入的不是左括号（此例中即右括号）
            if s.isEmpty():
                #栈为空，即右括号无左括号进行匹配，那么整个括号组成的字符串无法匹配
                matched = False
            else:
                s.pop()
                #栈不为空，即栈中有左括号与新输入的右括号匹配，左右括号匹配成功，栈删去一个存有的左括号
        index += 1

    if matched and s.isEmpty():
    #括号尽数匹配，一一对应
        return True
    else:
    #匹配失败
        return False

m = str(input())
print(parCheck(m))