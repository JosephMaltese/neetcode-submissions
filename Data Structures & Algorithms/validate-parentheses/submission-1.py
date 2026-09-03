class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching_brackets = {
            ")" : "(",
            "}": "{",
            "]": "["
        }
        
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if matching_brackets[char] != top:
                    return False
        if len(stack) == 0:
            return True
        return False
