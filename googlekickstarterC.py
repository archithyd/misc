lis_ans = []
for _ in range (int (input ( ))) :
    dic = {}
    n, k = map (int, input ( ).split ( ))
    lis = list (map (int, input ( ).split ( )))
    prime = 101
    val = []
    hash_org = 0
    hash_val = 0
    ans = 0
    for i in range (k, 0, -1) :
        val.append (i)
    hash_org = sum (val) % prime
    for i in range (0, n) :
        hash_val = sum (lis[i :i+k]) % prime
        if hash_val == hash_org :
            if val == lis[i :i+k] :
                ans += 1

    lis_ans.append (ans)

j = 1
for i in lis_ans :
    print ("Case #{0}: {1}".format(j,i))
    j += 1
