class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while len(stack) != 0 and stack[-1][1] < t:
                topItem = stack[-1]
                idx = topItem[0]
                res[idx] = i - idx
                stack.pop(-1)
            stack.append((i, t))
        return res
        