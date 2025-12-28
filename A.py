import heapq
import networkx as nx 
import matplotlib as plt 
end = [ ]
start = [ ] 
grid= [ ]
def heuristic_calc():
    man_dist = abs (a[0]- b[0]) + abs (a[1]-b[1])
    return man_dist 
def is_destination(row, column,end ):
    return (row == end[0]  and column == end[1])
       
def is_blocked(row, column):
    if (row == 0 and column ==0):
        return
def is_valid( row, column, grid):
    if (row >= 0 and row <= grid[0] and column >=0 and column <= grid[1]):


    

def A_star(grid, start, end):
    open_list = []
    
    open_list.append(start)
    closed_list = []
    path=[]
<<<<<<< HEAD
    open_list. remove(start)
    closed_list.append(start)
    # Initialize the current nodes 
    parent_row = start[0]
    parent_column = start[1]


    neighbours = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[1,0]]
    for k in neighbours:
        new_row  = parent_row + k[0]
        new_col = parent_column + k[1]
        if is_valid (new_row, new_col):
            if is_blocked(new_row, new_col):
                pass
            elif is_destination(new_row, new_col):
                print("The destination is found ")
                
    open_list.append(new_row, new_col)
        
        
        


    current_row = start[i]
    current_column = start[j]
    directions = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
    for dir in directions:
        row_neighbour = current_row + dir[0]
        column_neighbour  = current_column + dir[1]
        


