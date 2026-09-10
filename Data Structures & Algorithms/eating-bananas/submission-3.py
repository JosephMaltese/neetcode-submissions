import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        possibleAns = None

        while l<=r:
            mid = l + (r-l) // 2
            k=mid
            totalHrs = 0
            for p in piles:
                totalHrs += math.ceil(p/k)
            if totalHrs <= h:
                possibleAns = k
                r = mid-1
            else:
                l = mid+1
        return possibleAns
