def orderedSequentialSearch(alist, item):
    #定义初始查找位置，是否找到和是否停止的布尔变量
    pos = 0
    found = False
    stop = False
    #当没有彻查整个列表，也没有找到或停止时
    while pos < len(alist) and not found and not stop:
        #找到了指定元素，是否找到的布尔值返回为True
        if alist[pos] == item:
            found = True
        #当前位置没有找到指定元素
        else:
            #如果此时找到的元素比目标元素大，说明后面的所有元素都比目标元素大，则停止寻找
            if alist[pos] > item:
                stop = True
            #当前位置元素比目标元素小，继续检查下一位
            else:
                pos += 1

    return found