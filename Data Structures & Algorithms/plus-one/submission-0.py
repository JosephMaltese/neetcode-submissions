class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        carryOver = 1
        for i in range(len(digits)-1, -1, -1):
            plusOne = digits[i] + carryOver
            carryOver = plusOne // 10
            remainder = plusOne % 10
            res.append(remainder)
        if carryOver != 0:
            res.append(carryOver)
        res.reverse()
        return res
            
        