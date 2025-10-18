class OrderedList:
    def __init__(self):
        self.head = None

'''有序表的search方法'''#实现的原理上与无序表有一点差别，因此特地展示。下方add同理
def search(self,item):
    current = self.head
    found = False
    stop = False
    while current != None and not found and not stop:
        if current.getData() == item:
            found = True

        else:
            if current.getData() > item:
                stop = True
            else:
                current = current.getParent()

    return found

'''有序表的add方法'''
def add(self,item):
    current = self.head
    previous = None
    stop = False
    while current != None and not stop:
        if current.getData() > item:
            stop = True

        else:
            previous = current
            current = current.getParent()

    temp = Node(item)
    if previous == None:
        temp.setNext(self.head)
        self.head = temp

    else:
        temp.setNext(current)
        previous.setNext(temp)
