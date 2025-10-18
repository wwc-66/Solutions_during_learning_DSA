'''
算法思路：
对无序表进行多趟比较交换，
每趟包括了了多次两两相邻比较，并将逆序的数据项互换位置，
每趟的过程类似气泡在水中不断上浮。
'''
def bubbleSort(alist):
    #循环若干趟的排序过程。由于每次完成排序都会使最大项，次大项等依次就位，因此每次循环的总趟数会减少1次
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            #依次比较每个位置的元素与他的下一位元素的大小，如果比较元素为逆序，则交换位置
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]

'''
冒泡排序算法性能改进：

检测每趟比对是否发生过交换，
则可以提前确定排序是否完成，
省去重复的不必要对比
'''

def shortBubbleSort(alist):
    exchange = True
    passnum = len(alist)-1
    while passnum > 0 and exchange:
        exchange = False
        for i in range(passnum):
            #假设循环下来exchange始终为False，也就是已经交换过了，那么无需再重复排序，直接退出并返回结果
            if alist[i] > alist[i+1]:
                exchange = True
                alist[i], alist[i+1] = alist[i+1], alist[i]
        passnum -= 1