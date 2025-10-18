def sequentialSearch(alist,item):
    #设置当前查找的位置以及是否找到的布尔变量
    pos = 0
    found = False

    #当还没有完全找完整个列表并且目标尚未找到时
    while pos < len(alist) and not found:
        #如果找到，返回True
        if alist[pos] == item:
            found = True

        #没有找到，则继续下一位的查找
        else:
            pos += 1

    return found