ans=[]
for i in range(int(input())):
    lis = list(map(int, input().split()))
    if lis[0] == 1:
        ans.append(lis[1])
    elif lis[0] == 2:
        ans.pop(0)
    elif lis[0]==3:
        print(ans[0])
