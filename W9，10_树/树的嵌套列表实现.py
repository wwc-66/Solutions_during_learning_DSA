def BinaryTree(r):
    #创建一个只有根节点（值为r）和空子树的树
    return [r,[],[]]

def insertLeft(root,newBranch):
    #获取当前的左子树
    t = root.pop(1)
    #左子树不为空
    if len(t) > 1:
        #将原左子树变为插入左子节点的左子树，插入节点作为原左子树的根节点，再将新左子树接回原树
        root.insert(1,[newBranch,t,[]])
    #左子树为空，则直接将插入左子节点作为原左子树的根节点，再接回原树
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