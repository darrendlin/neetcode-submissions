class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        h = len(matrix)
        w = len(matrix[0])
        max_sq = 0
        
        res = [[-1] * w for i in range(h)]

        for i in range(h-1, -1, -1):
            for j in range(w-1, -1, -1):
                #print(i, j, res)
                if matrix[i][j] == "0":
                    res[i][j] = 0
                    continue
                right, down, diag = 0, 0, 0
                if j < w-1:
                    right = res[i][j+1]
                if i < h-1:
                    down = res[i+1][j]
                if right > 0 and down > 0:
                    diag = res[i+1][j+1]

                sq = 1 + min([right, down, diag])
                res[i][j] = sq
                max_sq = max(max_sq, sq)
                
        return max_sq**2
                