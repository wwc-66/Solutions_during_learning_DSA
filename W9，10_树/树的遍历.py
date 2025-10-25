def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

'''
上述为前序遍历（先访问根节点，再递归地前序访问左子树，最后前序访问右子树）
后序（先左，后右，最后根）和中序（先左，后根，最后右）遍历仅需调整顺序
'''

def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

def inorder(tree):
    if tree != None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())