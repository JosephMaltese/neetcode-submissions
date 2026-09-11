class Solution:
    def hammingWeight(self, n: int) -> int:
        oneCount = 0

        divisionRes = n

        while divisionRes != 0:
            remainder = divisionRes % 2
            if remainder == 1:
                oneCount += 1
            divisionRes = divisionRes // 2
        return oneCount