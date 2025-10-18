'''
2: 四柱汉诺塔
总时间限制: 1000
ms
内存限制: 65536
kB
描述
如课上所说，汉诺塔问题源于印度一个古老传说。对于原始的汉诺塔游戏，可供玩家操作的空间一共只有三根柱子，导致按原传说的要求，需要超过1
.8 * 10 ^ 19
步才能解开。

透过新增柱子可以大幅度地减少需要的步数。此处要求在给出指定的盘数，柱子数量为4（即限制为4根柱子）且不改变原有传说的其他规则的限制下，找出完成迁移的最小步骤数。

输入
一个非负整数M，M代表盘数，M <= 1000。
输出
一个非负整数，表示完成迁移的最小步骤数。
样例输入
3
样例输出
5
'''

def tower4(n,s,t,a1,a2):
    if n == 0:
        return []

    elif n == 1:
        return [f'将盘{n}从{s}移动到{t}']

    all_moves = []

    for i in range(n):
        moves = []
        moves.extend(tower4(i,s,a1,t,a2))
        moves.extend(tower3(n-i,s,t,a2))
        moves.extend(towe4(i,a1,t,s,a2))

        all_moves.append(moves)

    return min(all_moves)

def tower3(N,S,T,A):
    if N == 0:
        return []

    Moves = []

    Moves.extend(tower3(N-1,S,A,T))
    Moves.append(f'将盘{N}从{S}移动到{T}')
    Moves.extend(tower3(N-1,A,T,S))

    return Moves

num = int(input())

source = input()

auxiliary1 = input()

auxiliary2 = input()

target = input()

print(tower4(num,source,target,auxiliary1,auxiliary2))