def mergeSort(alist):
    if len(alist) > 1:
        #将原列表分为左右两部分并分别对其排序
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        #进行递归调用
        mergeSort(lefthalf)
        mergeSort(righthalf)

        #开始合并左右两列表
        i = j = k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1

            else:
                alist[k] = righthalf[j]
                j += 1

            k += 1

        #如果左右任意一部分还有剩余元素，则补进排好序的列表后面
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1

'''
上述代码是传统代码，可以实现功能，但下方将展示更加pythonnic的代码，更具可读性
'''

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    #取中点
    middle = len(lst)//2
    #对左右子列表进行递归调用，使左右两部分排好顺序
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])

    #初始化合并列表
    merged = []
    #当左右子表内同时还有元素时
    while left and right:
        #如果左子表第一位元素小于右子表第一位元素
        if left[0] < right[0]:
            #合并列表添加左子表第一位元素,同时删去这个元素
            merged.append(left.pop(0))
        #反之，添加右子列表第一位元素并在右子列表中删去该元素
        else:
            merged.append(right.pop(0))
    #将左右子表剩余的元素加到合并列表的末尾
    merged.extend(right if right else left)
    return merged