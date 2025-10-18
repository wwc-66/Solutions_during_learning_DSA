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

def hotPotato(namelist,num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)
        # 将输入的名单的名字依次输入队列中

    while simqueue.size() > 1:
        #当人数大于1时，热土豆一直传递下去
        for i in range(num):
            #输入的num是传递次数，最后一次拿到土豆的人退出队列
            simqueue.enqueue(simqueue.dequeue())
            #一次传递，即土豆传给下一个人后，上一个人会变成传递队列的最后一个人

        simqueue.dequeue()
        #当一轮num次传递结束时，拿到土豆的人退出队列，随后剩下的人继续传递土豆，直到只剩最后一人

    return simqueue.dequeue()#返回最后一个仅剩元素的值，满足此实例的核心要求

namelist1 = input().split(',')
num1 = int(input())
print(hotPotato(namelist1,num1))