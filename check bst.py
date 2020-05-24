import sys


def checkBST(root, min1, max1):
    if root is None:
        return True
    if root.data < min1 or root.data > max1:
        return False
    return checkBST(root.left, min1, root.data - 1) and checkBST(root.right, root.data + 1, max1)


def check_binary_search_tree_(root):
    checkBST (root, -sys.maxsize - 1, sys.maxsize)
