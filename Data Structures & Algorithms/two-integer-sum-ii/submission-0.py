class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l, r = 0, n-1

        while l < r:
            twoSum = numbers[l] + numbers[r]
            if twoSum == target:
                return [l+1, r+1]
            elif twoSum > target:
                r-=1
            else:
                l+=1