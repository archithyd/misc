n = int (input ( ))
lis = list (map (int, input ( ).split ( )))
count = 0
for i in range (n) :
    while lis[i] != i+1:
        temp = lis[i]
        lis[i] = lis[temp-1]
        lis[temp-1] = temp
        count += 1

print (count)
