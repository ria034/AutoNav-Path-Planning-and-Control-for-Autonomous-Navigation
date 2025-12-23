# AutoNav-Path-Planning-and-Control-for-Autonomous-Navigation
Developing a path planning algorithm( Dynamic A*,RRT) using python to avoid obstacles and for route optimization and testing it in  ROS2 and Gazebo, developed MPC and PID control algorithms using Python, reducing control errors by 25% and improving system stability by 15% 
A* algortihm basics :

# A* Path Planning Algorithm
## One-Sentence Intuition

> “A* identifies candidate states to explore, evaluates each using the sum of cost-so-far and estimated cost-to-go (f = g + h), and expands nodes in order of increasing f, ultimately reconstructing the optimal path once the goal is reached.”

## Overview
A* is a graph-based search algorithm used to find the **optimal path** from a start state to a goal state. It works by evaluating nodes based on the sum of:

- **g(n)** → cost from the start node to node `n` (actual cost so far)
- **h(n)** → estimated cost from node `n` to the goal (heuristic)

\[
f(n) = g(n) + h(n)
\]

---

## How A* Works (Intuition)

1. **Identify nodes (states)**
   - Each position/configuration is represented as a **node**.
   - The **open list** keeps track of all nodes discovered but not yet fully explored.

2. **Compute cost estimates**
   - For each node:
     - `g(n)` = actual cost from start to node
     - `h(n)` = estimated cost from node to goal
   - `f(n) = g(n) + h(n)` balances **progress made** with **distance to goal**.

3. **Select node with minimum f**
   - Choose the node with **lowest f** from the open list.
   - This ensures the **most promising path** is explored first.

4. **Expand the node**
   - Examine its neighbors (possible next steps)
   - Update their costs and parent pointers if a better path is found
   - Add them to the open list for future exploration

5. **Repeat until goal**
   - Continue until the goal node is reached
   - Reconstruct the path by backtracking through parent pointers

---

## Key Concepts

- **Open List**: All discovered nodes waiting to be expanded
- **Closed List**: Nodes already expanded
- **Heuristic (h)**: Must be **admissible** (never overestimates) for optimality
- **Optimality Guarantee**: A* finds the lowest-cost path if the heuristic is admissible and consistent

---



| Environment            | Heuristic            |
|------------------------|-------------------|
| 2D grid (4/8-connected)| Manhattan distance  |
| 2D grid (diagonal)     | Euclidean distance  |
| Car / non-holonomic     | Dubins distance    |
| Robot arm / joints      | Joint-space distance |

---



---

