import math
class Solution :
    # @param A : integer
    # @return an integer

    def trailingZeroes(self, A) :
        val = math.factorial(A)
        ans = 0
        p=5
        while A//p:
            ans+=A//p
            p*=5
        return ans

sol = Solution()
print(sol.trailingZeroes(5))