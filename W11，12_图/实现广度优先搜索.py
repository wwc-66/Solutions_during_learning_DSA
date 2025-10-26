def bfs(g, start):
    #起始顶点距离为0
    start.setDistance(0)
    #起始顶点无前驱顶点，因而设为None
    start.setPred(None)
    #创建队列，确保按照“先发现先探索的顺序”访问顶点
    vertQueue = Queue()
    #起始顶点入队
    vertQueue.enqueue(start)
    #队列长度大于0时持续探索
    while (vertQueue.size() > 0):
        #取队首作为当前顶点
        currentVert = vertQueue.dequeue()
        #遍历邻接顶点
        for nbr in currentVert.getConnections():
            #邻接顶点为白色，即未探索
            if (nbr.getColor() == 'white'):
                #颜色设为灰色，因为当前正在探索此邻接顶点
                nbr.setColor('grey')
                #当前顶点距离+1
                nbr.setDistance(currentVert.getDistance() + 1)
                #邻接顶点的前驱顶点设为当前顶点
                nbr.setPred(currentVert)
                #邻接顶点入队
                vertQueue.enqueue(nbr)
        #当前顶点设为黑色
        currentVert.setColor('black')

def setColor(self, color):
        self.color = color

def getColor(self):
        return self.color

def setDistance(self, dist):
        self.distance = dist

def getDistance(self):
        return self.distance

def setPred(self, pred):
        self.predecessor = pred

def getPred(self):
        return self.predecessor

def traverse(start,end):
    #创建列表，用于记录详细路径
    path = []
    #当前顶点为终点
    current = end
    #追踪到起点前
    while current != start:
        #记录路径上的每个顶点
        path.append(current.getId())
        #下一个追踪的顶点为当前顶点的前驱顶点
        current = current.getPred()
    #整体路径加上起点
    path.append(start.getId())
    #逆转路径列表顺序，呈现由起点到终点的路径
    path.reverse()
    return path