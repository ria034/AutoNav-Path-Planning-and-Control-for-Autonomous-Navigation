# AutoNav-Path-Planning-and-Control-for-Autonomous-Navigation
Developing a path planning algorithm( Dynamic A*,RRT) using python to avoid obstacles and for route optimization and testing it in  ROS2 and Gazebo, developed MPC and PID control algorithms using Python, reducing control errors by 25% and improving system stability by 15% 
A* algortihm basics :

Identify nodes (states)

In a well-defined environment, each position/configuration is represented as a node.

A* keeps track of which nodes have been discovered but not yet fully explored (the open list).

Compute cost estimates

For each node, compute:

𝑓
(
𝑛
)
=
𝑔
(
𝑛
)
+
ℎ
(
𝑛
)
f(n)=g(n)+h(n)

𝑔
(
𝑛
)
g(n) → cost from the start node to node 
𝑛
n (actual cost so far)

ℎ
(
𝑛
)
h(n) → estimated cost from node 
𝑛
n to the goal (heuristic)

This lets A* balance between progress made and remaining distance.

Select node with minimum f

The node with the lowest total estimated cost is chosen for expansion next.

This ensures we always explore the most promising path first.

Expand the node

Examine its neighbors (possible next steps)

Update their costs and parent pointers if a better path is found

Add them to the open list for future exploration

Repeat until goal

Continue this process until the goal node is reached

Reconstruct the path by backtracking through parent pointers
 What it needs? 
It needs discrete states/nodes defined. It would break in scenarios having continuous states as there are infinite numbers between (0-->1) which 

  
