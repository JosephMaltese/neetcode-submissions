class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l, r = 0, n-1
        max_area = 0

        while l<r:
            height_l = heights[l]
            height_r = heights[r]

            height = min(height_l, height_r)
            width = r-l
            area = width * height
            max_area = max(area, max_area)
            if height_l <= height_r:
                l+=1
            elif height_l > height_r:
                r-=1
        return max_area

        