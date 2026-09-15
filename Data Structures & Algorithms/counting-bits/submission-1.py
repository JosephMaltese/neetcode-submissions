class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        factor = 1
        def dp(i):
            nonlocal factor
            if i <= 0:
                return 0
            if i == factor * 2:
                factor *= 2
            return 1 + res[i-factor]
        for i in range(n+1):
            res.append(dp(i))
        return res

        