A=[1, 2, 5, -7, 2, 3]

maxsumlist = []
cursumlist = []
maxsum = 0
currsum = 0
for i in A :
    if (i >= 0) :
        currsum = currsum + i
        cursumlist.append (i)
        if (currsum > maxsum) :
            maxsum = currsum
            maxsumlist = cursumlist
        elif (currsum == maxsum) :
            if (len (cursumlist) > len (maxsumlist)) :
                maxsumlist = cursumlist
        

    elif (i < 0) :
        currsum = 0
        cursumlist = []
print(maxsumlist)
