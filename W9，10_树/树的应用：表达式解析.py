class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

def BinaryTree(r):
    return [r,[],[]]

def insertLeft(root,newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch,[],[]])

    return root

def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

'''上方先定义树和栈及其操作，便于下方实现代码的编写'''

'''
思路：
创建树的关键是对当前节点的跟踪
创建左右子树可调用insertRight/Left
当前节点设置值，可调用setRootVal
下降到左右子树可调用getLeft/RightChild

但上升到父节点没有可以直接调用来实现功能的函数
因此用一个栈来记录和跟踪父节点
当节点下降时，把下降前的节点push入栈。上升到父节点则出栈即可
'''
def buildParseTree(fpexp):
    #第一步创建一个字符串列表，分解原表达式
    fplist = fpexp.split()
    #创建一个保存节点的栈，用于后续上升父节点
    pStack = Stack()
    #创建一个空二叉树，节点值为空
    eTree = BinaryTree('')
    #当前节点入栈，最先创建的节点，最后再出栈
    pStack.push(eTree)
    #当前节点则为刚刚创建的节点
    currentTree = eTree
    #依次扫描表达式的每个字符
    for i in fplist:
        #表达式开始
        if i == '(':
            #创造一个左子节点
            currentTree.insertLeft('')
            #当前节点入栈，下降到左子节点
            pStack.push(currentTree)
            #当前节点变为左子节点
            currentTree = currentTree.getLeftChild()
        #操作数
        elif i not in ['+','-','*','/',')']:
            #当前节点设置成正在操作的数
            currentTree.setRootVal(int(i))
            #上升节点
            parent = pStack.pop()
            currentTree = parent
        #操作符号
        elif i in ['+','-','*','/']:
            #当前节点设为正在操作的符号
            currentTree.setRootVal(i)
            #下降到右子节点
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        #碰到右括号，即表达式结束
        elif i == ')':
            #出栈上升，返回到父节点
            currentTree = pStack.pop()
        #防止出错，表达式中出现不该出现的字符
        else:
            raise ValueError
    #返回创建的表达式的树
    return eTree