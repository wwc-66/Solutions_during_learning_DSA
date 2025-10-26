def genLegalMoves(x,y,bdSize):
    #创建列表，记录通过合法的走法移动后的新坐标
    newMoves = []
    #骑士所能走的方向和位置
    moveOffsets = [(-1,-2),(-1,2),(-2,-1),(-2,1),
                   (1,-2),(1,2),(2,-1),(2,1),]
    #遍历每一种走法，得到新的x和y坐标
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        #如果是合法的走法
        if legalCoord(newX,bdSize) and legalCoord(newY,bdSize):
            #加入newMoves列表
            newMoves.append((newX,newY))
    return newMoves

def legalCoord(x,bdSize):
    #确保骑士不会走出棋盘（合法走法）
    if x >= 0 and x < bdSize:
        return True
    else:
        return False

def knightGraph(bdSize):
    #创建空图
    ktGraph = Graph()
    #双重循环遍历棋盘上的每一个格子
    for row in range(bdSize):
        for col in range(bdSize):
            #定义骑士当前位置的编码（通过posToNodeId函数计算）
            nodeId = posToNodeId(row,col,bdSize)
            #通过合法走棋函数来获取合法走法移动后新坐标的位置
            newPositions = genLegalMoves(row,col,bdSize)
            #遍历每一个合法走法的新位置
            for e in newPositions:
                #定义骑士可以移动到的新位置的坐标的编码
                nid = posToNodeId(e[0],e[1],bdSize)
                #添加顶点和边
                ktGraph.addEdge(nodeId,nid)
    return ktGraph

def posToNodeId(row,col,bdSize):
    return row*bdSize + col