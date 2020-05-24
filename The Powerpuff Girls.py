n = int(input())
required = list(map(int, input().split()))
available = list(map(int,input().split()))
ans = 9999999999999
print(ans)
check = 0
for i in range(n):
    val = available[i]%required[i]
    check = (available[i]-val)//required[i]
    ans = min(ans,check)

print(ans)

"""
8
2 5 6 3 2 5 6 3
21 44 36 36 9 9 36 44
"""