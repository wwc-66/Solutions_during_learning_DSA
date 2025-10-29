'''
2:第一个坏版本
总时间限制: 1000ms 内存限制: 65536kB
描述
现在有同一个产品的N个版本，编号为从1至N的整数；其中从某个版本之后所有版本均已损坏。现给定一个函数isBadVersion，输入数字N可判断该版本是否损坏（若损坏将输出True）；请找出第一个损坏的版本。

注：有时isBadVersion函数运行速度很慢，请注意优化查找方式

输入
两行

第一行为整数，为产品号总数N

第二行为给定的判断函数，使用有效的Python表达式给出，可使用eval读取
输出
一行数字，表示第一个损坏的版本
样例输入
50
lambda n:n>=30
样例输出
30
'''

n = int(input())
isBadVersion = eval(input().strip())

def checker(N):
    #定义初始左右边界
    left = 1
    right = N
    #当左界小于右界，即还未锁定确定值时
    while left < right:
        #取中点
        mid = (left + right) // 2
        #如果中点处为坏版本，则右界前移
        if isBadVersion(mid):
            right = mid
        #中点处非坏版本，左界后移
        else:
            left = mid + 1
    #二分法最终找到第一个坏版本
    return left

print(checker(n))