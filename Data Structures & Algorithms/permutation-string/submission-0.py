class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        if s1_len > len(s2):
            return False

        s1_counts = defaultdict(int)
        for letter in s1:
            s1_counts[letter] += 1

        s2_counts = defaultdict(int)
        
        l=0
        for i in range(s1_len):
            s2_counts[s2[i]] += 1
        if s1_counts == s2_counts:
                return True

        for r in range(s1_len, len(s2)):
            s2_counts[s2[l]] -= 1
            if s2_counts[s2[l]] == 0:
                s2_counts.pop(s2[l], None)
            l+=1
            s2_counts[s2[r]] += 1
            if s1_counts == s2_counts:
                return True
        return False


        