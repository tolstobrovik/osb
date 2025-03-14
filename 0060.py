# https://leetcode.com/problems/permutation-sequence/description/

class Solution:
    def getPermutation(self, n: int, k: int):
        if n == 1:
            return '1'

        s = ''.join([str(i) for i in range(1, n + 1)])

        if k == 1:
            return s

        def factorial(n):
            if n == 0:
                return 1
            return n * factorial(n - 1)

        res = ''
        for i in range(1, n+1):
            if k == 1:
                res += s
                break
            step = factorial(n-i)
            ind = k // step
            res += s[ind]
            # print(k, s, ind, step)
            s = s.replace(s[ind], '')
            k = k - ind * step
        return res

a = Solution()
print(a.getPermutation(3, 3))
print(a.getPermutation(4, 9))
print(a.getPermutation(3, 1))