def _put(self,key,val,currentNode):
    #插入的节点键小于当前节点键
    if key < currentNode.key:
        #如果当前节点有左子节点
        if currentNode.hasLeftChild():
            #递归调用_put函数继续沿着当前节点的左子树向下延申最终确定位置
            self._put(key,val,currentNode.leftChild)
        #当前节点无左子节点
        else:
            #TreeNode函数新建节点，并将父节点指针指向当前节点
            currentNode.leftChild = TreeNode(key,val,parent = currentNode)
            #以刚刚插入的新节点为基础调整平衡因子
            self.updateBalance(currentNode.leftChild)
    #插入节点大于当前节点
    else:
        #如果当前节点有右子节点
        if currentNode.hasRightChild():
            #递归调用_put函数继续沿着当前节点的右子树向下延申最终确定位置
            self._put(key,val,currentNode.rightChild)
        #当前节点无右子节点
        else:
            #TreeNode函数新建节点，并将父节点指针指向当前节点
            currentNode.rightChild = TreeNode(key,val,parent = currentNode)
            #以刚刚插入的新节点为基础调整平衡因子
            self.updateBalance(currentNode.rightChild)

def updateBalance(self,node):
    #平衡因子大于1或小于-1
    if node.balanceFactor > 1 or node.balanceFactor < -1:
        #重新平衡
        self.rebalance(node)
        return
    #当前节点有父节点
    if node.parent != None:
        #当前节点为左子节点
        if node.isLeftChild():
            #其父节点的平衡因子+1
            node.parent.balanceFactor += 1
        #当前节点为右子节点
        elif node.isRightChild():
            #其父节点的平衡因子-1
            node.parent.balanceFactor -= 1
        #当前节点的父节点的平衡因子不为0
        if node.parent.balanceFactor != 0:
            #对当前节点的父节点递归调用updateBalance函数
            self.updateBalance(node.parent)

def rotateLeft(self,rotRoot):
    #新的根节点为旧根节点（rotRoot）的右子节点
    newRoot = rotRoot.rightChild
    #旧根节点的右子节点为新的根节点的左子节点（由于左旋之后，新的根节点的原左子节点大于旧根节点而小于新的根节点）
    #此处等号左右两边存在“时间差”，左边为左旋后，而右边为左旋前
    rotRoot.rightChild = newRoot.leftChild
    #新的根节点有左子节点
    if newRoot.leftChild != None:
        #新的根节点原先的左子节点的父节点指针指向旧根节点（因为左旋后它成为了旧根节点的右子节点）
        newRoot.leftChild.parent = rotRoot
    #新的根节点继承旧根节点的父节点（因为这可以只是一个子树）
    newRoot.parent = rotRoot.parent
    #如果旧根节点已经是根节点（非子树）
    if rotRoot.isRoot():
        #根节点更新为左旋后的新根节点
        self.root = newRoot
    #如果当前树为子树（旧根节点有父节点）
    else:
        #旧根节点为左子节点
        if rotRoot.isLeftChild():
            #旧根节点的父节点的左子节点指针指向新根节点
            rotRoot.parent.leftChild = newRoot
        #旧根节点为右子节点
        else:
            #旧根节点的父节点的右子节点指针指向新根节点
            rotRoot.parent.rightChild = newRoot
    #左旋后，新根节点的左子节点为旧根节点
    newRoot.leftChild = rotRoot
    #左旋后，旧根节点的父节点指针指向新根节点
    rotRoot.parent = newRoot
    #重新计算新旧根节点的平衡因子
    rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor,0)
    newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor,0)

def rotateRight(self,rotRoot):
    #新的根节点为旧根节点（rotRoot）的左子节点
    newRoot = rotRoot.leftChild
    #旧根节点的左子节点为新的根节点的右子节点（由于右旋之后，新的根节点的原右子节点小于旧根节点而大于新的根节点）
    #此处等号左右两边存在“时间差”，左边为右旋后，而右边为右旋前
    rotRoot.leftChild = newRoot.rightChild
    #新的根节点有右子节点
    if newRoot.rightChild != None:
        #新的根节点原先的右子节点的父节点指针指向旧根节点（因为右旋后它成为了旧根节点的左子节点）
        newRoot.rightChild.parent = rotRoot
    #新的根节点继承旧根节点的父节点（因为这可以只是一个子树）
    newRoot.parent = rotRoot.parent
    #如果旧根节点已经是根节点（非子树）
    if rotRoot.isRoot():
        # 根节点更新为右旋后的新根节点
        self.root = newRoot
    #如果当前树为子树（旧根节点有父节点）
    else:
        #旧根节点为左子节点
        if rotRoot.isLeftChild():
            #旧根节点的父节点的左子节点指针指向新根节点
            rotRoot.parent.leftChild = newRoot
        #旧根节点为右子节点
        else:
            #旧根节点的父节点的右子节点指针指向新根节点
            rotRoot.parent.rightChild = newRoot
    #右旋后，新根节点的右子节点为旧根节点
    newRoot.rightChild = rotRoot
    #右旋后，旧根节点的父节点指针指向新根节点
    rotRoot.parent = newRoot

def rebalance(self,node):
    #当前节点右重，需要左旋
    if node.balanceFactor < 0:
        #当前节点的右子节点左重，先对右子节点右旋
        if node.rightChild.balanceFactor > 0:
            self.rotateRight(node.rightChild)
            #然后再左旋
            self.rotateLeft(node)
        #直接左旋
        else:
            self.rotateLeft(node)
    #当前节点左重，需要右旋
    elif node.balanceFactor > 0:
        #当前节点的左子节点右重，先左旋
        if node.leftChild.balanceFactor < 0:
            self.rotateLeft(node.leftChild)
            #然后再右旋
            self.rotateRight(node)
        #直接右旋
        else:
            self.rotateRight(node)