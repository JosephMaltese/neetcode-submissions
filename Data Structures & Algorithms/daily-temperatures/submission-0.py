class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for i in range(len(temperatures))]
        stack = []

        for i in range(len(temperatures)):
            while len(stack) != 0 and stack[-1][1] < temperatures[i]:
                topItem = stack[-1]
                idx = topItem[0]
                res[idx] = i - idx
                stack.pop(-1)
            stack.append((i, temperatures[i]))
        return res
        