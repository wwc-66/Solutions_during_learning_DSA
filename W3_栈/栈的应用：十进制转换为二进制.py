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

def divideBy2(n):
    s = Stack()
    while n > 0 :
    #对输入的数字n不断地除2取余（不是0就是1）存入栈中
        rem = n % 2
        s.push(rem)
        n = n // 2

    outcome = ''
    #从尾到头取出栈中的0，1.由于计算时，大数除2取余先入栈，因此输入数字的二进制结果要将栈中0和1反向取出
    while not s.isEmpty():
        outcome += str(s.pop())

    return outcome

num = int(input())
print(divideBy2(num))