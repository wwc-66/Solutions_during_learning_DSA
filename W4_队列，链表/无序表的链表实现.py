class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, data):
        self.data = data

    def setNext(self, next):
        self.next = next

class UnoderedList:
    def __init__(self):
        self.head = None

'''无序表的add方法'''
def add(self,item):
    temp = Node(item)
    temp.setNext(self.head)
    self.head = temp
    #此处末两句代码次序不可颠倒

'''无序表的size方法'''
def size(self):
    current = self.head
    count = 0
    while current != None:
        count += 1
        current = current.getNext()

    return count

'''无序表的search方法'''
def search(self,item):
    current = self.head
    found = False
    while current != None and not found:
        if current.getData() == item:
            found = True
        else:
            current = current.getNext()

    return found

'''无序表的remove方法'''
def remove(self,item):
    current = self.head
    previous = None
    found = False
    while not found:
        if current.getData() == item:
            found = True
        else:
            previous = current
            current = current.getNext()

    if previous == None:
        self.head = current.getNext()

    else:
        previous.setNext(current.getNext())