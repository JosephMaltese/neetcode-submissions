class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1 for i in range(len(nums))]
        postfix = [1 for i in range(len(nums))]
        res = []

        for i in range(len(nums)):
            if i == 0:
                prefix[i] = nums[i]
            else:
                prefix[i] = prefix[i-1] * nums[i]
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                postfix[i] = nums[i]
            else:
                postfix[i] = postfix[i+1] * nums[i]
        for i in range(len(nums)):
            if i == 0:
                pre = 1
            else:
                pre = prefix[i-1]
            if i == len(nums)-1:
                post = 1
            else:
                post = postfix[i+1]
            res.append(pre*post)
        return res

        