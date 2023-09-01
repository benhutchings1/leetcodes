from typing import List
from collections import deque

def numIslands(grid: List[List[str]]) -> int:
    unvisited = []
    visited = {}
    # Change surrounding numbers
    def alt_surr(val, y, x):
        # Mark position as visited
        visited[(y,x)] = True
        # Directions of surrounding
        dir = [
            [-1, 0],
            [0, -1],
            [1, 0],
            [0, 1]
        ]
        # Get all new directions x,y
        locs = [(int(y)+yadd, int(x)+xadd) for yadd, xadd in dir]
        # Change values of new directions
        for ynew, xnew in locs:
            # Check within bounds of grid
            if (ynew >= 0) and (xnew >= 0) and\
                (ynew < len(grid)) and (xnew < len(grid[0])):
                    # Change if island not if ocean or discovered island
                    if grid[ynew][xnew] == "1":
                        # Check if position has already been checked
                        if (ynew, xnew) not in visited:
                            unvisited.append((ynew, xnew))
                        grid[ynew][xnew] = str(val)
    # Initialise starting position
    nxt = (0, 1)
    grid[nxt[1]][nxt[0]] = "2"
    
    # Visit each block at a time and check surrounding
    while True:
        print(unvisited)
        alt_surr(2, nxt[1], nxt[0])
        # Move to next block
        nxt = unvisited.pop()  
        if len(unvisited) == 0:
            break  

    return grid

def disp_grid(grid):
    for y in grid:
        for x in y:
            print(x, end=" ")
        print()

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
disp_grid(numIslands(grid))