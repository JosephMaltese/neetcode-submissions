class Solution:
    memo = {}
    def rob(self, nums: List[int]) -> int:
        key = tuple(nums)
        if key in self.memo.keys():
            return self.memo[key]
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        if len(nums) == 3:
            return max(nums[1], nums[0]+nums[2])
        res = max(nums[0]+ self.rob(nums[2:]), nums[1] + self.rob(nums[3:]))
        self.memo[key] = res
        return res
        