class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # 1 = land
        # 0 = water
        # visited
        # iterate every piece
        # count = 0
        # DFS
        
        def explore (grid, r, c, visited):
            if r not in range(len(grid)) or c not in range(len(grid[0])):
                return False
            
            if grid[r][c] == "0":
                return False
            
            pos = (r, c)
            if pos in visited:
                return False       

            visited.add(pos)
                       
            explore (grid, r-1, c, visited)
            explore (grid, r+1, c, visited)
            explore (grid, r, c-1, visited)
            explore (grid, r, c+1, visited)          

            return True
        
        visited = set()
        count = 0
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (explore(grid, r, c, visited) == True):
                    count = count + 1
                    
        return count
        
        