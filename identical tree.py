class Node:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None


def identicalTrees(temp1, temp2):
    if temp1 is None and temp2 is None:
        return True
    if temp1 is not None and temp2 is not None:
        return temp1.val == temp2.val and (identicalTrees(temp1.left,temp2.left)) and (identicalTrees(temp1.right,temp2.right))
    return False


root1 = Node(1)
root2 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)

root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)
root2.left.right = Node(5)

if identicalTrees(root1, root2 ):
    print("Both trees are identical")
else:
    print("Trees are not identical")