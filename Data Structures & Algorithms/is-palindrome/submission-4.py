class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = ''.join(c.lower() for c in s if c.isalnum())

        n = len(letters)
        if n == 0 or n == 1:
            return True
        left, right = 0, n-1
        while letters[left] == letters[right] and left < right:
            left+=1
            right-=1
        return not (left < right)