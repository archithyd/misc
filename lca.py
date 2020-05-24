"""def lca(root, v1, v2):
  if root is None:
      return None
  if v1 == root.info or v2 == root.info:
      return root.info
  left = lca(root.left,v1,v2) #the returned value of the left child node
  right = lca(root.right,v1,v2) #the returned value of the roght child node
  if left != None and right != None:
      return root
  if left == None and right == None:
          return None
  if left!=None and right == None:
      return left
  if left == None and right != None :
      return right
"""

def list_creater(root,val):
    lis=[]
    if root is None:
        return
    else:
        if val>root.info:
            lis.append (root.info)
            return (lca (root.right, val))
        else:
            lis.append(root.info)
            return(lca(root.left,val))
    return lis


def lca(root,v1,v2):
    if root is None:
        return
    lv1=list_creater(root,v1)
    lv2 = list_creater (root, v2)

    for (i,j) in zip(lv1,lv2):
        if i!=j:
            print(i)
            break
