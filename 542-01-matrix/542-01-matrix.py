class Solution:    
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # need to implement DP
        m, n = len(mat), len(mat[0]) # rows, cols
        
        # iter 1: up -> down, use left + up vals to calculate distances
        for i in range(m):
            for j in range(n):
                if mat[i][j] != 0:
                    mat[i][j] = float('inf') # initialize: set to large number
                    if (i-1) >= 0 and mat[i-1][j] + 1 < mat[i][j]: # up
                        mat[i][j] = mat[i-1][j] + 1
                    if (j-1) >= 0 and mat[i][j-1] + 1 < mat[i][j]: # left
                        mat[i][j] = mat[i][j-1] + 1
                        
        # iter 2: down -> up, use right and down vals
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if mat[i][j] != 0:
                    if (i+1) < m and mat[i+1][j] + 1 < mat[i][j]:
                        mat[i][j] = mat[i+1][j] + 1
                    if (j+1) < n and mat[i][j+1] + 1 < mat[i][j]:
                        mat[i][j] = mat[i][j+1] + 1
        
        return mat