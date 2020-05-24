class newnode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None


def existPath(temp, lis):
    q=[]
    if temp is None:
        return 0
    q = []
    len1 = len(lis)
    len2 = 0
    q.append(temp)
    while(len(q)):
        val = q.pop(0)
        len2+=1
        if val.data == lis[0]:
            lis.pop(0)
            if val.left:
                if val.left.data == lis[0]:
                    q.append(val.left)
            if val.right:
                if val.right.data == lis[0]:
                    q.append(val.right)
    if len2 == len1:
        return 1
    else:
        return 0





if __name__ == '__main__' :

    # arr[] -. sequence of root to leaf path
    arr = [5, 8, 6, 7]
    n = len (arr)
    root = newnode (5)
    root.left = newnode (3)
    root.right = newnode (8)
    root.left.left = newnode (2)
    root.left.right = newnode (4)
    root.left.left.left = newnode (1)
    root.right.left = newnode (6)
    root.right.left.right = newnode (7)

    if existPath (root, arr):
        print("yes")
    else:
        print("no")