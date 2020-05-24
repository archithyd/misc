class Node :
    def __init__(self, info) :
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self) :
        return str (self.info)


class BinarySearchTree :
    def __init__(self) :
        self.root = None

    def create(self, val) :
        if self.root == None :
            self.root = Node (val)
        else :
            current = self.root

            while True :
                if val < current.info :
                    if current.left :
                        current = current.left
                    else :
                        current.left = Node (val)
                        break
                elif val > current.info :
                    if current.right :
                        current = current.right
                    else :
                        current.right = Node (val)
                        break
                else :
                    break


# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 


       // this is a node of the tree , which contains info as data, left , right
'''


def list_creater(root, val):
    lis = []
    cur = root
    while(cur.info != val):
        if val==cur.info:
            lis.append(val)
        elif val>cur.info:

            lis.append(cur.info)
            cur=cur.right
        else:
            lis.append(cur.info)
            cur=cur.left
    return lis



        # if val > root.info :
        #     lis.append (root.info)
        #     return (list_creater (root.right, val))
        # else :
        #
        #     lis.append (root.info)
        #     return (list_creater (root.left, val))


def lca(root, v1, v2) :
    if root.info == v1 or root.info == v2:
        print(root.info)
    lv1 = list_creater (root, v1)
    lv2 = list_creater (root, v2)
    # if len(lv1)<len(lv2):
    #     print(lv1[len(lv1)-1])
    # else:
    #     print(lv2[len(lv2)-1])
    if min(len(lv1),len(lv2)) == 1:
        for i, j in zip (lv1, lv2) :
             if i == j :
                 print (i)
                 break
    else:
        print("hi")
        print(lv1)
        print(lv2)
        for i, j in zip (lv1, lv2) :
             if i != j :
                 print (i)
                 break

tree = BinarySearchTree ( )
t = int (input ( ))

arr = list (map (int, input ( ).split ( )))

for i in range (t) :
    tree.create (arr[i])

v = list (map (int, input ( ).split ( )))

ans = lca (tree.root, v[0], v[1])
