# AutoNav-Path-Planning-and-Control-for-Autonomous-Navigation
Developing a path planning algorithm( Dynamic A*,RRT) using python to avoid obstacles and for route optimization and testing it in  ROS2 and Gazebo, developed MPC and PID control algorithms using Python, reducing control errors by 25% and improving system stability by 15% 
A* algortihm basics :

# A* Path Planning Algorithm
## One-Sentence Intuition

> “A* identifies candidate states to explore, evaluates each using the sum of cost-so-far and estimated cost-to-go (f = g + h), and expands nodes in order of increasing f, ultimately reconstructing the optimal path once the goal is reached.”
In this project:
> The files are
>  A_shortest_path_list.py --> A* with open list containing the nodes that we are about to explore as dictionaries so as to get the minimum values of heuristics
> A_shortest_path_heap.py --> A* with open list containing the nodes that we are about to explore stores in priority queues or heaps(data structures)
> A_star_visualization --> Consists of grid to visualize the path, the start and end nodes.
>
Yet to implement : 
RRT --> Based sampling based motion planning to see 
And also RL to select heuristic based on the number of directions we are going to move in 


