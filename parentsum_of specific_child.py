class getNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

def Sum1(temp,k):
    if temp is None:
        return
    q = []
    q.append(temp)
    ans=0

    while len(q):
        count = 0
        val = q.pop(0)
        if val.left:
            q.append(val.left)
        if val.right:
            q.append(val.right)
        if val.left:
            if val.left.data == k and count == 0:
                ans+=val.data
                count=1
        if val.right:
            if val.right.data == k and count == 0:
                ans+=val.data
                count=1

    return ans


if __name__ == '__main__' :
    # binary tree formation
    root = getNode (4)  # 4
    root.left = getNode (2)  # / \
    root.right = getNode (5)  # 2 5
    root.left.left = getNode (2)  # / \ / \
    root.left.right = getNode (2)  # 7 2 2 3
    root.right.left = getNode (2)
    root.right.right = getNode (3)

    x = 2

    print ("Sum = ", Sum1(root, x))