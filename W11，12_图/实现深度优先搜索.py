'''以骑士周游问题为例，展示第一种DFS的代码'''
def knightTour(n,path,u,limit):
    #n为层次，path为路径，u为当前顶点，limit为搜索深度
    #当前顶点设为灰色（正在访问）
    u.setColor('grey')
    #当前顶点加入路径path列表
    path.append(u)
    #当前层次（即当前顶点深度）小于搜索限制深度limit时，继续搜索
    if n < limit:
        #获取当前顶点的所有邻接顶点
        nbrList = list(u.getConnections())
        #设定访问次数的循环值（即邻接顶点的数量）
        i = 0
        done = False
        #遍历所有邻接顶点直到找到解或全部遍历
        while i < len(nbrList) and not done:
            #检查当前邻接顶点是否被访问过
            if nbrList[i].getColor() == 'white':
                #递归调用，深度+1，继续从该邻接顶点搜索
                done = knightTour(n+1,path,nbrList[i],limit)
            #移动到下一个邻接顶点
            i += 1
        #当前分支路径未找到解，则从路径中移除当前顶点并将颜色设为白色（可重新访问）
        #当前顶点虽然在这条路径上无解，但有可能出现在另一条有解路径上，因此重设为白色
        if not done:
            path.pop()
            u.setColor('white')
    #n >= limit，说明找到完整路径，设置完成标志done
    else:
        done = True
    return done

'''
算法改进
第一版运行时间高度取决于棋盘大小，并且差距非常大
新算法仅修改了遍历下一格的次序
在第一版代码中，对于下一个顶点的搜索顺序完全随机
而第二版代码，先搜索可达路径更短更少的顶点，再去搜索分支相对复杂的顶点
'''

def orderByAvail(n):
    #初始化结果列表，用于存储形为（可用移动数，顶点）的元组
    resList = []
    #遍历当前顶点n的所有邻接顶点v
    for v in n.getConnections():
        #只考虑未被访问过的邻接顶点
        if v.getColor() == 'white':
            #初始化计数器，用于计算顶点v的可用移动数
            c = 0
            #遍历顶点v的所有邻接顶点w
            for w in v.getConnections():
                #如果邻接顶点w未被访问过，则计数器+1
                #此处计算的是从v出发还能移动到多少个未访问的顶点
                if w.getColor() == 'white':
                    c += 1
            #将（可用移动数，顶点）元组添加到结果列表
            resList.append((c,v))
    #按照可用移动数进行升序排序
    resList.sort(key=lambda x:x[0])
    return [y[1] for y in resList]