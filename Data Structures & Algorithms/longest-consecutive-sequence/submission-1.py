class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_sequence_len = 0
        s = set(nums)
        for num in nums:
            left_neighbor = num-1
            if left_neighbor in s:
                continue
            next_num = num+1
            sequence_len = 1
            while next_num in s:
                sequence_len += 1
                next_num+=1
            longest_sequence_len = max(longest_sequence_len, sequence_len)
        return longest_sequence_len