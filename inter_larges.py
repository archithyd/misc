A = [3, 1, 2, 5, 3]

A = sorted(A)
ans = [0,0]
A_val = 0
B_val = 0
diff= 0
count = []

for i in range(len(A)):
    count.append(i+1)


for i in range(0,len(A)-1):
    if A[i] == A[i+1]:
        A_val = A[i]
diff = sum(A) - sum(count)

B_val = A_val-diff
ans[:] = [A_val,B_val]
print(ans)