n=1011
lis=[]
num=0
i=0
while n!=0:
    num+=pow(2,i)*(n%10)
    n=n//10
    i+=1
print(num)
print(int(format(n,"b"),2))