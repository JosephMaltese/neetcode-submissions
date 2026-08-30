class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        chars = list(s)

        l,r = 0,1

        seen = set()
        seen.add(chars[l])
        current_len = 1
        longest_substr_len = 1
        while r < len(chars):
            if chars[r] not in seen:
                seen.add(chars[r])
                r+=1
                current_len+=1
                longest_substr_len = max(current_len, longest_substr_len)
            else:
                while chars[l] != chars[r]:
                    seen.remove(chars[l])
                    current_len-=1
                    l+=1
                current_len-=1
                seen.remove(chars[l])
                l+=1
        return longest_substr_len

        