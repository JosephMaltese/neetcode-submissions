class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        top, bottom = 0, m - 1

        targetRow = None
        while top < bottom:
            mid = top + (bottom -  top) // 2
            midRow = matrix[mid]
            midRange = [midRow[0], midRow[n-1]]

            if target >= midRange[0] and target <= midRange[1]:
                targetRow = midRow
                print(targetRow)
                break
            elif target < midRange[0]:
                bottom = mid-1
            else:
                top = mid+1
        if not targetRow:
            targetRow = matrix[top]
        
        l, r = 0, n - 1
        while l < r:
            mid = l + (r-l) // 2

            if target == targetRow[mid]:
                return True
            elif target > targetRow[mid]:
                l = mid+1
            else:
                r = mid-l
        if l == r:
            return targetRow[l] == target
        return False
        