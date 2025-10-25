class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

class TreeNode:
    def __init__(self,key,val,left = None,right = None,parent=None):
        self.key = key #键值
        self.payload = val #包含的数据项
        self.leftChild = left
        self.rightChild = right
        self.parent = parent #指向父节点

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.leftChild or self.rightChild)

    def hasAnyChildren(self):
        return self.leftChild or self.rightChild

    def hasBothChildren(self):
        return self.leftChild and self.rightChild

    def replaceNodeData(self,key,value,lc,rc):
        #更新节点的新键，新值以及子节点关系
        self.key = key#设置新键
        self.payload = value#设置新值
        self.leftChild = lc#设置新的子节点
        self.rightChild = rc#设置新的右节点
        #当前节点已有左子节点
        if self.hasLeftChild():
            #将左子节点的父节点指针指向当前节点
            self.leftChild.parent = self
        #原理同上，仅方向改变
        if self.hasRightChild():
            self.rightChild.parent = self

    def put(self,key,val):
        #检查树是否为空
        if self.root:
            #如果不为空，调用递归函数从根节点开始插入
            self._put(key,val,self.root)

        else:
            #树为空，创建根节点
            self.root = TreeNode(key,val)
        #树的大小增加1
        self.size += 1

    def _put(key,val,currentNode):
        #当插入键小于当前节点键时
        if key < currentNode.key:
            #检查当前节点是否有左子节点
            if currentNode.hasLeftChild():
                #有左子节点，递归调用_put到左子树
                self._put(key,val,currentNode.leftChild)
            else:
                #没有左子节点，创建新节点作为左子节点并设置父节点指针
                currentNode.leftChild = TreeNode(key,val,parent = currentNode)

        #插入键大于当前节点的键
        else:
            #检查当前节点是否含有右子节点
            if currentNode.hasRightChild():
                #有右子节点，递归调用_put到右子树
                self._put(key,val,currentNode.rightChild)


            else:
                #无右子节点，创建新节点作为右子节点并设置父节点指针
                currentNode.rightChild = TreeNode(key,val,parent = currentNode)

    def __setitem__(self,key,val):
        self.put(key,val)

    def get(self,key):
        #检查树是否为空
        if self.root:
            #调用递归函数进行查找
            res = self._get(key,self.root)
            #找到节点，则返回节点存储的值。否则返回None
            if res:
                return res.payload
            else:
                return None

        else:
            return None

    def _get(self,key,currentNode):
        #当前节点为空，即没有找到，则返回None
        if not currentNode:
            return None
        #找到目标节点（即当前节点）
        elif currentNode.key == key:
            return currentNode
        #如果要找的键小于当前节点键，则在左子树中继续查找。反之在右子树中查找
        elif key < currentNode.key:
            return self._get(key,currentNode.leftChild)
        else:
            return self._get(key,currentNode.rightChild)

    def __getitem__(self,key):
        return self.get(key)

    def __contains__(self,key):
        if self._get(key,self.root):
            return True
        else:
            return False

    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for elem in self.leftChild:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem

    def delete(self,key):
        #判断当前树大小是否为1

        #当树的大小比1大时
        if self.size > 1:
            #先找到需要remove的节点，再调用remove删除
            nodeToRemove = self._get(key,self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size -= 1

            else:
                raise KeyError('Error, key not in tree')

        #树只剩下一个节点即根节点时
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1

        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self,key):
        self.delete(key)
        #没有子节点
        if currentNode.isLeaf():
            #如果是左子节点
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            #如果是右子节点
            else:
                currentNode.parent.rightChild = None

        #仅有一个子节点
        else:
            #当前节点有左子节点
            if currentNode.hasLeftChild():

                #当前节点为左子节点
                if currentNode.isLeftChild():

                    #当前节点的左子节点的父节点指向当前节点的父节点
                    currentNode.leftChild.parent = currentNode.parent

                    #当前节点的父节点的左子节点指向当前节点的左子节点
                    currentNode.parent.leftChild = currentNode.leftChild

                #当前节点为右子节点
                elif currentNode.isRightChild():

                    #当前节点的左子节点的父节点指向当前节点的父节点
                    currentNode.leftChild.parent = currentNode.parent

                    #当前节点的父节点的右子节点指向当前节点的左子节点
                    currentNode.parent.rightChild=currentNode.leftChild

                #当前节点为根节点
                else:

                    #将当前节点即根节点的键和值全部设为其左子节点，且原左子节点的左右子节点指针指向更新后的根节点
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                                currentNode.leftChild.payload,
                                                currentNode.leftChild.leftChild,
                                                currentNode.leftChild.rightChild)

            #当前节点有右子节点
            else:
                #当前节点为左子节点
                if currentNode.isLeftChild():
                    #当前节点的右子节点的父节点指向当前节点的父节点
                    currentNode.rightChild.parent = currentNode.parent
                    #当前节点父节点的左子节点指向当前节点的右子节点
                    currentNode.parent.leftChild = currentNode.rightChild
                #当前节点为右子节点
                elif currentNode.isRightChild():
                    #当前节点右子节点的父节点指向当前节点的父节点
                    currentNode.rightChild.parent = currentNode.parent
                    #当前节点的父节点的右子节点指向当前节点的右子节点
                    currentNode.parent.rightChild = currentNode.rightChild
                #当前节点为根节点
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                                                currentNode.rightChild.payload,
                                                currentNode.rightChild.leftChild,
                                                currentNode.rightChild.rightChild)

        #当前节点同时有左右子节点
        elif currentNode.hasBothChildren():
            #找到currentNode的后继节点
            succ = currentNode.findSuccessor()
            #把succ节点摘出
            succ.spliceOut()
            #当前节点的键值替换为succ的
            currentNode.key = succ.key
            currentNode.payload = succ.payload

    #寻找后继节点
    def findSuccessor(self):
        succ = None
        #如果当前节点有右子节点
        if self.hasRightChild():
            #以当前节点的右子节点为根节点，沿着右子节点的左子树找到最小值（通过findMin函数实现）
            succ = self.rightChild.findMin()
        #当前没有右子节点
        else:
            #当前节点有父节点
            if self.parent:
                #当前节点为父节点的左子节点
                if self.isLeftChild():
                    #后继节点为父节点
                    succ = self.parent
                #当前节点为父节点的右子节点
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    def findMin(self):
        #定义当前节点
        current = self
        #当前节点有左子节点时
        while current.hasLeftChild():
            #当前节点指针更新到左子节点
            current = current.leftChild
        #当最终定位到最小的叶节点时，返回此节点
        return current

    def spliceOut(self):
        #当前节点为叶节点（即无子节点）,直接摘除
        if self.isLeaf():
            #当前节点为左子节点
            if self.isLeftChild():
                #摘除此节点
                self.parent.leftChild = None
            #当前节点为右子节点
            else:
                #摘除此节点
                self.parent.rightChild = None
        #当前节点有子节点时
        elif self.hasAnyChildren():
            #当前节点有左子节点
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            #当前节点有右子节点
            else:
                #当前节点为左子节点
                if self.isLeftChild():
                    #摘除当前节点，其父节点与子节点指针指向对方
                    self.parent.leftChild = self.rightChild
                #当前节点为右子节点
                else:
                    #原理同上，仅方向改变
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent