f = open("mongodb.py", "r")
values = f.readlines()
f.close()
val=[2,3,4,5,6,7,8,7,8,9,10]
ans=0
for i in range(len(val)):
    if i == val[i]:
        ans+=1
print(ans)



