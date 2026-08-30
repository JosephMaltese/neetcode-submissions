class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                break
            l, r = i+1, n-1
            while l<r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
                elif threeSum > 0:
                    r-=1
                else:
                    l+=1
        return res
        