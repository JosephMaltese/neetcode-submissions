class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequencies = defaultdict(int)

        num_replacements = 0
        l = 0
        longest = 0

        for r in range(len(s)):
            current_char = s[r]
            frequencies[current_char] += 1

            while (r-l+1) - max(frequencies.values()) > k:
                frequencies[s[l]] -= 1
                l+=1
            longest = max(longest, r-l+1)
        return longest