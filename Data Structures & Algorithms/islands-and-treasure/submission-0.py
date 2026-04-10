class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(0,1), (0, -1), (1, 0), (-1, 0)]
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(r, c):
            q = deque()
            q.append((r,c))
            distance = 1
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row+dr, col+dc
                    if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] != -1:
                        if grid[row][col] + 1 < grid[nr][nc]:
                            grid[nr][nc] = grid[row][col] + 1 
                            q.append((nr,nc))
                    
                            

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    bfs(r,c)
        

