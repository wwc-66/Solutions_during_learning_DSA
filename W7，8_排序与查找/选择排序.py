def selectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax = 0
        for location in range(1,fillslot+1):
            #当发现逆序时，不直接互换位置，而是在当前一次循环中标记较大项的位置并作为“目前最大项”，
            #直到最终找到真正的最大项，才进行位置的改变
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location

        alist[positionOfMax] , alist[fillslot] = alist[fillslot] , alist[positionOfMax]