'''
4:求素数个数
总时间限制: 1000ms 内存限制: 16384kB
描述
输入两个数a，b，计算在[a,b]范围内，有多少个素数。

输入
2行，每行一个正整数
输出
一个数，表示素数个数
样例输入
5
10
样例输出
2
'''
a = int(input())
b = int(input())
prime_lst = []

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

for i in range(a, b+1):
    if is_prime(i):
        prime_lst.append(i)
print(len(prime_lst))