class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_letters = "abcdefghijklmnopqrstuvwxyz0123456789"
        letters = list(s.lower())
        letters = list(filter(lambda x: x in valid_letters, letters))

        n = len(letters)
        if n == 0 or n == 1:
            return True
        left, right = 0, n-1
        while letters[left] == letters[right] and left < right:
            left+=1
            right-=1
        return not (left < right)