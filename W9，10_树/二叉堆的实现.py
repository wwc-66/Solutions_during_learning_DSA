class BinHeap:
    def __init__(self):
        #初始化堆，但需要使根节点的下标从1开始，因此整个堆的非嵌套列表需要有一个0放在里面来占据0下标
        self.heaplist = [0]
        #初始堆的大小为0
        self.currentSize = 0

    def percUp(self, i):
        while i // 2 > 0:
            #如果当前节点比它的父节点小，则与父节点交换，使当前节点上浮。（辅助下方的insert函数使用）
            if self.heaplist[i] < self.heaplist[i // 2]:
                self.heaplist[i],self.heaplist[i // 2] = self.heaplist[i // 2],self.heaplist[i]
            #依次上浮，直到当前节点处于它本该在的节点位置
            i = i // 2

    def minChild(self, i):
        #如果minChild是唯一子节点，则直接返回
        if i * 2 + 1 > self.currentSize:
            return i * 2
        #如果minChild不是唯一子节点，则与另一子节点比较后再返回最小值
        else:
            if self.heaplist[i * 2] < self.heaplist[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def percDown(self, i):
        #当节点i还有子节点时i，继续循环
        while (i * 2) <= self.currentSize:
            #找到i的子节点中的更小的那个
            mc = self.minChild(i)
            #如果当前节点比子节点大
            if self.heaplist[i] > self.heaplist[mc]:
                #则交换并继续下沉
                self.heaplist[i],self.heaplist[mc] = self.heaplist[mc],self.heaplist[i]
            #更新节点位置，继续检查
            i = mc

    def insert(self,key):
        #新key添加到末尾
        self.heaplist.append(key)
        self.currentSize += 1
        #新key上浮
        self.percUp(self.currentSize)

    def delMin(self):
        #移走堆的顶
        retval = self.heaplist[1]
        #将堆顶设为最后一个叶节点
        self.heaplist[1] = self.heaplist[self.currentSize]
        #由于移走了堆顶，因此整个堆的大小减1
        self.currentSize -= 1
        #去掉最后一个叶节点，因为上方只是把堆顶设为最后一个叶节点的相同值，所以此处需要pop()掉来达到“移动”的效果
        self.heaplist.pop()
        #新的顶开始下沉
        self.percDown(1)
        return retval

    def bulidHeap(self,alist):
        #从最后节点的父节点开始下沉
        i = len(alist)//2
        #设置当前堆的大小
        self.currentSize = len(alist)
        self.heaplist = [0] + alist[:]
        print(len(self.heaplist),i)
        #从最后一个父节点开始，向前遍历到根节点1
        while i > 0:
            print(self.heaplist[i],i)
            #当前节点下沉，以满足堆的性质
            self.percDown(i)
            #移动到前一个节点
            i -= 1
        print(self.heaplist,i)