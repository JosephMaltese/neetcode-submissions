class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        items = list(counts.items())
        items.sort(key=lambda x: x[1], reverse=True)
        res = []

        for i in range(k):
            res.append(items[i][0])

        return res
