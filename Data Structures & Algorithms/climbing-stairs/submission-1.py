class Solution:
    memo = {}
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        if n in self.memo.keys():
            return self.memo[n]
        sol = self.climbStairs(n-2) + self.climbStairs(n-1)
        self.memo[n] = sol
        return sol
        