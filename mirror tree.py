class newNode:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def areMirrors(temp1,temp2):
    if temp2 is None and temp1 is None:
        return True

    if temp1 is not None and temp2 is not None:
        return temp1.data==temp2.data and (areMirrors(temp1.left,temp2.right)) and (areMirrors(temp1.right,temp2.left))
    return False

if __name__ == '__main__' :
    # 1st binary tree formation
    root1 = newNode (1)  # 1
    root1.left = newNode (2)  # / \
    root1.right = newNode (2)  # 3    2
    root1.right.left = newNode (5)  # / \
    root1.right.right = newNode (4)  # 5      4

    # 2nd binary tree formation
    root2 = newNode (1)  # 1
    root2.left = newNode (2)  # / \
    root2.right = newNode (3)  # 2     3
    root2.left.left = newNode (4)  # / \
    root2.left.right = newNode (5)  # 4  5

    print (areMirrors (root1, root2))