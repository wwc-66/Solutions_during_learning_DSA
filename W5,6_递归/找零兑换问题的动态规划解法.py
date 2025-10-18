def dpMakeChange(coinValueList,change,minCoins):
    #从一分钱开始到change逐个计算最少硬币数
    for cents in range(1,change+1):
        #初始化一个最大值
        coinCount = cents
        #减去每个硬币，向后查找最少硬币数，同时记录总的最少数
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
        #得到当前最少硬币数，记录到表中
        minCoins[cents] = coinCount
    #返回最后一个结果
    return minCoins[change]