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
    # Initialize the current nodes 
    current_row = start[i]
    current_column = start[j]
    for i in range()



