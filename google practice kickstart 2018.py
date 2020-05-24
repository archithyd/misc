def checker(num):
    count=0
    np=0
    while(num>0):
        val=num%10
        if val%2==0:
            count+=1
        num=num//10
        np+=1
    if count==np:
        return 1
    else:
        return -1


num =2020
add=0
# sub=0
loopadd=-1
while(loopadd<1):
     print("hi1")
     loop1=checker(num+1)
     add+=1
     if loop1 == 1:
         loopadd=True
         break
     else:
         loopadd=-1
print(add)
# loopsub=False
# while(loopsub!=True):
#     print("hi")
#     loop1=checker(num-1)
#     sub+=1
#     if loop1 == "True":
#         loopsub=True
#         break
#
# if add<sub:
#     print(add)
# else:
#     print(sub)