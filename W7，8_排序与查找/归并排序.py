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

    middle = len(lst)//2
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])

    merged = []
    while left and right:
        if left[0] < right[0]:
            merged.append(left[0])

        else:
            merged.append(right[0])

    merged.extend(right if right else left)
    return merged