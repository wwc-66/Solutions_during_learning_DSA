def binarySearch(alist, item):
    #定义初末位置和是否找到的布尔变量
    first = 0
    last = len(alist) - 1
    found = False
    #没有找到目标元素并且查找区间不断缩小直到仅含一个元素
    while first <= last and not found:
        #二分法确定区间中点
        midpoint = (first + last) // 2
        #如果中点恰好是目标元素，返回True
        if alist[midpoint] == item:
            found = True
        #中点不是目标元素时
        else:
            #目标小于中点值，将区间缩小到原区间的前半部分
            if item < alist[midpoint]:
                last = midpoint - 1
            #目标大于中点值，将区间缩小到原区间的后半区间
            else:
                first = midpoint + 1

    return found