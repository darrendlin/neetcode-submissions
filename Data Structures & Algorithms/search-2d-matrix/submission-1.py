class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        for row in matrix:
            if target >= row[0] and target <= row[-1]:
                left = 0
                right = cols-1
                middle = (right + left) // 2

                while right >= left:
                    if row[middle] == target:
                        return True
                    if row[middle] > target:
                        right = middle-1
                    elif row[middle] < target:
                        left = middle+1
                    middle = (right + left) // 2
                return False
        return False