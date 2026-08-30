from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letters_count_s = defaultdict(int)
        letters_count_t = defaultdict(int)

        for letter in s:
            letters_count_s[letter] += 1
        for letter in t:
            letters_count_t[letter] += 1
        
        for letter, count in letters_count_s.items():
            if count != letters_count_t[letter]:
                return False
        return True
