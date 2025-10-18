class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

def palchecker(aString):
    chardeque = Deque()
    for ch in aString:
        #将输入的字符依次输入到队列中
        chardeque.addRear(ch)

    stillEqual = True

    while chardeque.size() >1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        #同时取出首末字符检查是否相同
        if first != last:
            #当提取的首末字符不同时，返回false
            stillEqual = False

    return stillEqual

s = input()
print(palchecker(s))