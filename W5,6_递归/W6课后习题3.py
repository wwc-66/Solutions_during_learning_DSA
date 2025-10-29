'''
3:表达式按不同顺序求值
总时间限制: 500ms 内存限制: 65536kB
描述
给定一个表达式字符串，求出按不同的求值顺序可能得到的所有结果


示例代码模板：

def findWays(expr):
    # 用于将字符串转为数字与运算符，供参考
    nums, ops = [], []
    num = 0
    for c in expr:
        if '0' <= c <= '9':
            num = num * 10 + ord(c) - 48
        else:
            ops.append(c)
            nums.append(num)
            num = 0
    else:
        nums.append(num)

    # code here

expr=input()
print(findWays(expr))


输入
一行字符串，仅包含0-9与运算符+、-与*

注：字符串保证三种运算符左右均为数字字符
输出
所有不重复的可能的结果，从小到大排序并以半角逗号","分隔
样例输入
2*3-4*5
样例输出
-34,-14,-10,10
提示
注：

(2*(3-(4*5))) = -34

((2*3)-(4*5)) = -14

((2*(3-4))*5) = -10

(2*((3-4)*5)) = -10

(((2*3)-4)*5) = 10
'''

def findWays(expr):
    #创建列表，储存数字
    numbers = []
    #创建列表，储存运算符
    operators = []
    #设置当前数字变量
    current_num = ''
    # 遍历输入表达式的每个字符
    for ch in expr:
        #如果是数字，添加到当前数字字符串
        if ch in '1234567890':
            current_num += ch
        #如果是运算符
        else:
            #把当前数字加入数字列表
            numbers.append(int(current_num))
            #当前运算符加入运算符列表
            operators.append(ch)
            #重置当前数字字符串，输入后续数字
            current_num = ''
    #对于最后一个数字，由于其后无运算符，因此不会在for循环中被添加到数字列表中
    #故最后一个数字在循环结束后需要手动添加
    numbers.append(int(current_num))

    def calculate_all(left,right):
        #如果只有一个数字，直接返回此数字
        if left == right:
            return [numbers[left]]
        #储存所有可能的结果
        all_results = []
        #在每个运算符处分割出左右两个子式
        for i in range(left,right):
            #获取当前运算符
            op = operators[i]
            #递归计算左右子式
            left_results = calculate_all(left,i)
            right_results = calculate_all(i+1,right)
            #组合左右结果并计算
            for left_val in left_results:
                for right_val in right_results:
                    if op == '+':
                        result =  left_val + right_val
                    elif op == '-':
                        result =  left_val - right_val
                    elif op == '*':
                        result = left_val * right_val
                    #将结果加入所有结果列表中
                    all_results.append(result)
        return all_results
    #计算所有可能结果
    #初始调用：计算整个表达式
    all_possible = calculate_all(0,len(numbers)-1)
    #使用字典去重
    unique_results = {}
    for result in all_possible:
        unique_results[result] = True
    #排序并转换成字符串列表
    sorted_res = sorted(unique_results.keys())
    string_res = [str(x) for x in sorted_res]
    #用逗号连接所有结果
    return ','.join(string_res)

exp=input()
print(findWays(exp))