lis_ans=[]
a = "aaabba"
ans = -9999999
val_ans = None
for i in range(len(a)):
    val=""
    for j in range(i,len(a)):
        val +=a[j]
        if val == val[::-1]:
            if len(val)>ans:
                ans = len(val)
                val_ans = val
lis_ans.append(val_ans)

for i in lis_ans:
    print(i)
