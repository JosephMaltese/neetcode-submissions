import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) >= 2:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)

            if x == y:
                continue
            
            if x < y:
                y = y - x
                heapq.heappush(stones, -y)
            else:
                x = x - y
                heapq.heappush(stones, -x)
        if len(stones) > 0:
            return -stones[0]
        return 0
            
        