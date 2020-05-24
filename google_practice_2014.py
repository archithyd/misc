def printer(ans) :
    ran = len (ans)
    for i in range (ran) :
        if ans[i] == -1 :
            print ("Case #",i+1,":","Yes")
        else :
            print ("Case #",i+1,":","No")


def checker(grp1, grp2) :
    count = 0
    for x in grp1 :
        if x in grp2 :
            if grp1[x] == grp2[x] :
                count += 1
            else :
                break
        else :
            pass
    if count == n :
        return 1
    else :
        return -1


def dict_creater(lis1, lis2) :
    dic1 = {}
    dic2 = {}
    for i, j in zip (lis1, lis2) :
        if i in dic1 :
            dic1[i] += 1
        else :
            dic1[i] = 1
        if j in dic2 :
            dic2[j] += 1
        else :
            dic2[j] = 1
    return checker (dic1, dic2)


if __name__ == "__main__" :
    lis_ans = []
    for i in range (int (input ( ))) :
        n = int (input ( ))
        lis11 = []
        lis22 = []
        for j in range (n) :
            n1, m1 = map (str, input ( ).split ( ))
            lis11.append (n1)
            lis22.append (m1)
        lis_ans.append (dict_creater (lis11, lis22))
    printer (lis_ans)
