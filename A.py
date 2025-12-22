import heapq
import networkx as nx 
import matplotlib as plt 
 
def heuristic_calc():
    man_dist = abs (a[0]- b[0]) + abs (a[1]-b[1])
    return man_dist 

def A_star(grid, start, end):
    open_list = []
    
    heapq.heappush (open_list,(0,start))
    closed_list = { }
    path=[]
    current_row = start[i]
    current_column = start[j]
    directions = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
    for dir in directions:
        row_neighbour = current_row + dir[0]
        column_neighbour  = current_column + dir[1]
        if 



