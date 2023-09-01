from typing import List
from collections import deque
import numpy as np

def numIslands(grid: List[List[str]]) -> int:
    '''
    Returns the number of islands. Islands are disconnected by ocean and islands are connected by cardinally adjacent 1's

            Parameters:
                    Grid (List[List[str]]): Grid containing island (1) and ocean (0) values

            Returns:
                    (int): Number of islands
    '''
    # Input validation
    if grid is None:
        return 0

    unvisited = deque([])
    visited = {}
    def change_surr(y:int, x:int, newval:int):
        '''
        Changes cardinally adjacent island from given starting coordinates and adds new island values to undiscovered array
        
        Parameters:
                    y (str): y value of starting coordinates
                    x (str): x value of starting coordinates
                    newval (str): value to change cardinally adjacent islands to

            Returns:
                    (int): Number of islands
        '''
        # Check if coord has already been visited
        if (y,x) in visited:
            return
        # Add coord to visited
        visited[(y,x)] = True
        # Define all directions
        dirs = [[-1, 0],[0, -1],[1, 0],[0, 1]]
        for ydir, xdir in dirs:
            # Get coords in direction
            ynew = y + ydir
            xnew = x + xdir
            # Check if new coords are on grid
            if (ynew >= 0) and (xnew >= 0) and\
                (ynew < len(grid)) and (xnew < len(grid[0])):
                    # Check if new coord is island
                    if grid[ynew][xnew] != "0":
                        # Update new coord
                        grid[ynew][xnew] = newval
                        # Add new coord to unvisited
                        unvisited.append((ynew, xnew))
    
    def grid_where():
        '''Search grid for undiscovered island and returns new coordinates'''
        xlen = len(grid[0])
        for y in range(len(grid)):
            for x in range(xlen):
                if grid[y][x] == "1":
                    # Return coords
                    return (y,x)
        # return no island found
        return None

    # Store number of islands
    no_islands = 1
    # Iterate until all island are found
    while True:
        # Find new undiscovered island
        nxt = grid_where()
        # If no island found break
        if nxt is None:
            break
        else:
            # Add new island
            no_islands += 1
            grid[nxt[0]][nxt[1]] = no_islands

        while True:
            # Apply analysis to given coords
            change_surr(nxt[0], nxt[1], no_islands)
            # Check if unvisited list is empty
            if len(unvisited) == 0:
                break  
            # Get new coords
            nxt = unvisited.pop()

    return no_islands - 1


def disp_grid(grid):
    '''Display grid'''
    for y in grid:
        for x in y:
            print(x, end=" ")
        print()

print("Grid:")
grid = []
disp_grid(grid)
print()
print(f"Number of islands: {numIslands(grid)}")