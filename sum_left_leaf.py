class Node :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None


def left(temp):
    if temp is None:
        return
    q = []
    q.append(temp)
    ans = 0
    while len(q):
        val = q.pop(0)
        if val.left is not None:
            q.append(val.left)
            if val.left.left is None or val.right.left is None:
                ans += val.data
        if val.right:
            q.append(val.right)
    return ans






root = Node(20)
root.left = Node(9)
root.right = Node(49)
root.right.left = Node(23)
root.right.right = Node(52)
root.right.right.left = Node(50)
root.left.left = Node(5)
root.left.left.left = Node(10)
root.left.left.left.left=Node(10)
root.left.right = Node(12)
root.left.right.right = Node(12)
print("Sum of left leaves is", left(root) )