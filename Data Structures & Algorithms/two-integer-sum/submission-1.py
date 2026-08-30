class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_idx_map = {}

        for i in range(len(nums)):
            num = nums[i]
            remainder = target - num

            if remainder in value_idx_map.keys():
                return [value_idx_map[remainder], i]
            if num not in value_idx_map.keys():
                value_idx_map[num] = i
        