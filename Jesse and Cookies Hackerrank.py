import heapq as heap
def sweetner(arr,k1):
    count = 0
    heap.heapify(arr)
    while(arr[0]<k1):
        if len(arr)==1:
            count = -1
            break
        else:
            c1=heap.heappop(arr)
            c2=heap.heappop (arr)
            heap.heappush (arr, 1*c1 + 2 * c2)
            count+=1
    return count


if __name__=="__main__":
    n,k = map(int,input().split())
    lis = list(map(int, input().split()))
    print(sweetner(lis,k))
