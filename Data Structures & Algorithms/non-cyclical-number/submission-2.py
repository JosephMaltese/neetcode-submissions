class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            strN = str(n)
            totalSum = 0
            for digit in strN:
                totalSum += (int(digit)) ** 2
            n = totalSum
        if n == 1:
            return True
        return False
        