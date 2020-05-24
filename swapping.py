def swap(arr):
    temp=arr[0]
    arr[0]=arr[1]
    arr[1]=temp
    return arr


def inorder(arr1):
    ans=[]
    inorder(arr1)
    ans.append()


def list_convertor(arr1):
    list1=[1]
    for i,j in arr1:
            list1.append(i)
            list1.append(j)
    print(list1)
    return inorder(list1)


def traverse(arr,val):
    cur = val
    if val>1:
        while(cur>val-2):
            arr[cur]=swap(arr[cur])
            cur=cur-1
        list_convertor(arr)
    else:
        arr[0]=swap(arr[1-1])
        list_convertor(arr)


def swapNodes(indexes, queries):
    for i in queries:
        traverse(indexes,i)




if __name__ == '__main__':
    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

