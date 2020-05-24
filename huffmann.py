list1=[]

def value(root,code):
    if root is None:
        return
    elif code == "0":
        list1.append(value(root.left,code))
    else:
        list1.append(value(root.right,code))

def decodeHuff(root, s):
    for i in s:
        if i == 1:
            value(root.right,i)
        else:
            value(root.left,i)
    print(list1)
