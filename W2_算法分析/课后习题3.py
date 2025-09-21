'''
3:判断素数
总时间限制: 1000ms 内存限制: 16384kB
描述
输入一个正整数n，编程判断n是否是素数。

输入
一个正整数
输出
是素数，输出"yes"，否则输出"no”。
（注意输出不包括引号）
样例输入
11
样例输出
yes
'''
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

num = int(input())
if is_prime(num):
    print('yes')
else:
    print('no')