'''
3:ASCII谢尔宾斯基地毯
总时间限制: 1000ms 内存限制: 65536kB
描述
谢尔宾斯基地毯一种正方形分形图案，每个地毯可分为等大小的9份，其中中央挖空，其余均由更小的地毯组成。

现给定地毯大小（行数）与组成地毯的字符元素，请打印相应的地毯图形。

注：空腔以半角空格表示；当给定字符元素长度不为1时空格数须与字符长度对应

输入
输入为两行，分别为地毯大小正整数N与组成元素字符串c

输入数据保证N为3的正整数幂
输出
由N行长度为N*len(c)的字符串构成的谢尔宾斯基地毯
样例输入
9
[]
样例输出
[][][][][][][][][]
[]  [][]  [][]  []
[][][][][][][][][]
[][][]      [][][]
[]  []      []  []
[][][]      [][][]
[][][][][][][][][]
[]  [][]  [][]  []
[][][][][][][][][]
'''

'''
思路：先画出实心图像，随后通过递归不断挖空
'''

def sierpinski_carpet(N,c):
    #得到初始地毯，后续将进行挖空操作
    carpet = [c * N for _ in range(N)]
    #定义挖空操作函数
    def recursive_draw(x,y,size):
        if size < 3:
            return
        #计算子正方形边长大小
        sub_size = size // 3
        #挖空正方形中心
        for row in range(y+sub_size,y+2*sub_size):
            #计算挖空范围
            start_col = (x+sub_size) * len(c)
            end_col = (x+2*sub_size) * len(c)
            #对字符串重新赋值达到挖空效果
            carpet[row] = carpet[row][:start_col] + ' '*(len(c)*sub_size) + carpet[row][end_col:]

        #对其他八个子正方形进行挖空操作
        for i in range(3):
            for j in range(3):
                #跳过中心子正方形（已被全部挖空）
                if i == 1 and j == 1:
                    continue
                #计算在递归调用中的x，y坐标
                new_x = x + i * sub_size
                new_y = y + j * sub_size
                #递归调用
                recursive_draw(new_x,new_y,sub_size)
    #从大正方形开始递归挖空
    recursive_draw(0,0,N)
    return carpet

C = input()
n = int(input())
carpet0 = sierpinski_carpet(n,C)
for ch in carpet0:
    print(ch)

'''提交答案运行时间超出题目要求，但功能可正常实现'''