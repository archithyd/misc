lis_ans = []
for _ in range(int(input())):

    n = int(input())
    G_Revolution = list(map(int, input().split()))
    All_Starz = list(map(int, input().split()))
    ans = 0
    All_Starz.sort(reverse=1)
    G_Revolution.sort(reverse=1)
    while len(All_Starz) !=0:
        val_G = G_Revolution[0]
        val_A = All_Starz[0]
        All_Starz.pop(0)
        if val_G>val_A:
            ans+=1
            G_Revolution.pop(0)
    lis_ans.append(ans)


for i in lis_ans:
    print(i)


