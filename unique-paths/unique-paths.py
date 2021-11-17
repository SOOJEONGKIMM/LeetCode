class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #DP
        grid = [[0]*m for i in range(n)]
        direction = [(0,-1),(-1,0)]
        
        for i in range(n):
            for j in range(m):
                if i==0 or j==0:
                    grid[i][j]=1
                    continue
                    
                for next_pos in direction:
                    next_n, next_m = next_pos
                    tmp_n = i + next_n
                    tmp_m = j + next_m
                    
                    if tmp_n < 0 or tmp_m < 0 or n<=tmp_n or m<=tmp_m:
                        continue
                    
                    grid[i][j] += grid[tmp_n][tmp_m]
                    
        return grid[n-1][m-1]