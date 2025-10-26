class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        #nbr为顶点对象的key
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + 'connectedTo:' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    #新加顶点
    def addVertex(self,key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    #通过key寻找顶点
    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost = 0):
        #新加边的起点和终点若为不存在的顶点，则先添加顶点
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList,cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

def buildGraph(wordFile):
    d = {}
    g = Graph()
    wfile = open(wordFile,'r')#此处wordFile为外部下载的含有大量单词的文件
    #创建装有仅一字母之差的单词的“桶”
    for line in wfile:
        #去除换行符
        word = line.strip()
        #依次剔除各位置的字母
        for i in range(len(word)):
            #剔除索引为i的字母，例如当i=0，单词为word，则此时bucket为“_ord”
            bucket = word[:i] + '_' + word[i+1:]
            #如果当前桶已在d中则把当前单词放入桶中
            if bucket in d:
                d[bucket].append(word)
            #如果当前桶不在d中，则新建一个值为含有当前单词的列表的“桶”键
            else:
                d[bucket] = [word]
    #同一个桶内的单词之间建立边edge
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                #桶内两个单词互不相同则建边edge
                if word1 != word2:
                    g.addEdge(word1,word2)
    return g