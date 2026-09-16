class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        sum1 = 0
        for i in range(n+1):
            sum1 += i
        sum2 = 0
        for num in nums:
            sum2 += num
        return sum1 - sum2