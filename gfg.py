def number0f2s(n) :
    num = n
    ans = 0
    while num > 0 :
        mod = num % 10
        num = num // 10
        if mod == 2 :

            ans += 1
    return ans


def numberOf2sinRange(n) :
    val = 0
    for i in range (n + 1) :
        val += number0f2s (i)
    return val

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        print(numberOf2sinRange(n))