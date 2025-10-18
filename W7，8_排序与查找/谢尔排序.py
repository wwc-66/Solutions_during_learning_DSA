def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentValue = alist[i]
        position = i

        while position >= gap and alist[position-gap] > currentValue:
            alist[position] = alist[position-gap]
            position = position-gap

        alist[position] = currentValue

'''
上述代码是另一种插入排序的实现代码，
只不过间隔由默认的1变为了可以任意选择的gap，
服务于下方的谢尔排序功能
'''

def shellSort(alist):
    #设定初始的间隔
    sublistcount = len(alist)//2
    #不断地去缩小间隔并将子列表进行排序
    while sublistcount > 0:
        #排序子列表
        for startposition in range(sublistcount):
            gapInsertionSort(alist,startposition,sublistcount)

        #进一步缩小间隔
        sublistcount = sublistcount // 2