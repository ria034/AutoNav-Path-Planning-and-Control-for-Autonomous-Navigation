import heapq
import networkx as nx 
import matplotlib as plt 
 
def heuristic_calc(start, stop):
    man_dist = abs (stop[0]- start[0]) + abs (stop[1]-start[1])
    return man_dist 

def A_star(grid, start, stop): 
    open_nodes_list = []                                 # keeps all the nodes that needs to be expanded
    closed_nodes_list = []                            # keeps all the nodes that are expanded/ explored 
    path = []                                       # stores the nodes with minimum heuristics
    open_nodes_list.append(start)
    path.append(start)
    tentative_g = 1
    heur = 0
    parent_row = path [0]
    parent_column = path [1]
    directions = [(1,0),]
    for d in directions:                         # this loop is made to compute the cost of each neighbouring node 
        new_row = parent_row + d[0]
        new_col = parent_column + d[1]
        parent= [ new_row, new_col]
        if parent in closed_nodes_list:
            return
        elif parent is stop:
            print ("The destination is found")
            path.append(parent)
        else:
    
            tentative_g = tentative_g + 1
            heuristic = heuristic_calc (parent, stop)
            open_nodes_list.append(parent, heuristic)
            current =min (open_nodes_list, key=lambda x:x[0])
            path.append (current)



    
        
       





    



