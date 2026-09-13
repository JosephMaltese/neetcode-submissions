import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        for point in points:
            x = point[0]
            y = point[1]

            distance = math.sqrt((0-x)**2 + (0-y)**2)
            heapq.heappush(heap, (distance, point))
        
        for i in range(k):
            item = heapq.heappop(heap)
            res.append(item[1])
        return res

        