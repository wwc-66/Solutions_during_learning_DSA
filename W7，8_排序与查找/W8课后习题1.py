'''
1:字符串中所有重排
总时间限制: 500ms 内存限制: 65536kB
描述
给定一个字符串s与待查找字符串p，请给出使得s[i:i+len(p)]是p的一个字母重排的所有下标i

题目保证字符串p非空，且各字符串仅由小写字母构成

参考代码模板：

def findAnagrams(s, p):
    # code here
    pass

s = input()
p = input()
findAnagrams(s, p)

输入
两行字符串，第一行为s，第二行为p
输出
所有满足条件的下标从小到大排列，以空格分隔输出

若无对应下标，则输出字符串"none"
样例输入
abababa

ab
——————————
a

b
样例输出
0 1 2 3 4 5
——————————
none
'''