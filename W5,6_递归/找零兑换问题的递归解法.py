def recMC(coinValueList,change):
    #初始化最坏的情况，即最小硬币数等于找零金额（全部用1兑换）
    minCoins = change
    #找零金额刚好等于某面值的硬币时
    if change in coinValueList:
        return 1
    else:
        #只查找那些小于等于需找零金额的面值的硬币
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMC(coinValueList,change - i)
            #更新最小硬币数
            if numCoins < minCoins:
                minCoins = numCoins

    return minCoins

'''
上述代码运行效率极低，主要原因在于做了大量重复计算，浪费较多时间。因此作出如下改动：
'''

def recDC(coinValueList,change,knownResults):
    minCoins = change
    #找零金额刚好等于某面值的硬币时
    if change in coinValueList:
        #记录结果到缓存
        knownResults[change] = 1
        return 1
    elif knownResults[change] > 0:
        return knownResults[change]
    else:
        #只查找那些小于等于需找零金额的面值的硬币
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recDC(coinValueList,change - i,knownResults)
            #更新最优解
            if numCoins < minCoins:
                minCoins = numCoins
                knownResults[change] = minCoins

    return minCoins