class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        subsets = self.subsets(nums[1:])
        first = nums[0]
        with_first = [sub + [first] for sub in subsets]
        return subsets + with_first
        