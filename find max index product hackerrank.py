
#NOT COMPLETED
"""
def RIGHT(list1, val) :
    dic = {}
    for i in range (len (list1)) :
        if list1[i] in dic :
            dic[list1[i]] = i
        else :
            dic[list1[i]] = i
    print(dic)
    return dic[val]


def LEFT(list1, val) :
    dic = {}
    for i in range (len (list1)) :
        if list1[i] in dic :
            dic[list1[i]] = i
        else :
            dic[list1[i]] = i
    print(dic)
    return dic[val]


n = int (input ( ))
lis = list (map (int, input ( ).split ( )))
max1 = 0

for i in range (1, n - 1) :
    if max (lis[0 :i]) > lis[i] :
        left = LEFT (lis[0 :i], max (lis[0 :i]))
    else :
        left = 0
    if max (lis[i :n]) > lis[i] :
        right = RIGHT (lis[i :n], max (lis[i :n]))
    else :
        right = 0
    indexproduct = (left+1) * (right+(len(lis[:i])+1))
    print(indexproduct)
    if indexproduct > max1 :
        max1 = indexproduct
print (max1)
"""


n=5
lis=[5,4,3,4,5]
max1=0
for i in range(1,n-1):
    left=0
    right=0
    for j,z in zip(lis[i-1:-1:-1],range(len(lis[:i]))):
        print(j,z)
        if lis[i]<j:
            left=z
            print(left)
            break
    print("blank")
    for k,y in zip(lis[i:n],range(len(lis[i:]))):
        print(k,y)
        if lis[i]<k:
            right=y
            break
    index_product = left*right
    if index_product > max1 :
        max1 = index_product
print(max1)




