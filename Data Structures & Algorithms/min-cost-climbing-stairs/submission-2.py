class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def dfs(idx):
            if idx > len(cost)-1:
                return 0
            if idx in memo.keys():
                return memo[idx]
            ans = cost[idx] + min(dfs(idx+1), dfs(idx+2))
            memo[idx] = ans
            return ans
        
        return min(dfs(0), dfs(1))
        