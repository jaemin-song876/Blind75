class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        m, n = len(heights), len(heights[0])

        pac_queue = deque()
        for col in range(n):
            pac_queue.append((0, col))
        for row in range(m):
            pac_queue.append((row, 0))

        atl_queue = deque()
        for col in range(n):
            atl_queue.append((m-1,col))
        for row in range(m):
            atl_queue.append((row,n-1))

        pac_visited = set()
        atl_visited = set()
        
        def bfs(queue, visited):
            while queue:
                (row, col) = queue.popleft()
                visited.add((row, col))

                for dr, dc in [(0,1),(0,-1), (1,0),(-1,0)]:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr <= m-1 and 0 <= nc <= n-1 and (nr, nc) not in visited and heights[nr][nc] >= heights[row][col]:
                        queue.append((nr,nc))
                        visited.add((nr,nc))
        bfs(pac_queue, pac_visited)
        bfs(atl_queue, atl_visited)            
        return [[r,c] for r,c in pac_visited & atl_visited]





        