def solve_maze(maze):
    rows, cols = len(maze), len(maze[0])
    path = [[False] * cols for _ in range(rows)]
 
    def search(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols:
            return False
        if maze[r][c] == 1 or path[r][c]:
            return False
 
        path[r][c] = True
        if r == rows - 1 and c == cols - 1:
            return True
 
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if search(r + dr, c + dc):
                return True
 
        path[r][c] = False
        return False
 
    if search(0, 0):
        for r in range(rows):
            print(" ".join("P" if path[r][c] else
                           "#" if maze[r][c] == 1 else "."
                           for c in range(cols)))
    else:
        print("No path found.")
 
maze = [
    [0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
solve_maze(maze)
