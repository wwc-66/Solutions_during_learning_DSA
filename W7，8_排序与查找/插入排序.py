def insertionSort(alist):
    #循环每个元素
    for index in range(1, len(alist)):
        #当前需要插入的值
        currentValue = alist[index]
        position = index
        #当前一项比需要插入的值小时，互换位置，将正在操作的值不断前移
        while position > 0 and alist[position-1] > currentValue:
            alist[position] = alist[position-1]
            position = position - 1
        #当终于找到前一项比它小的位置时，退出while循环并将操作的值插入最终找到的位置
        alist[position] = currentValue