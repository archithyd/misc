word1 = "eat"
word2 = "sea"

if len(word1) == 0:
    print(len(word2))
elif len(word2) == 0:
    print(len(word1))
else:
    val = list(set(word1)&set(word2))
    ans = min(len(val),max(len(word1),len(word2))-len(val))
    print(ans)
