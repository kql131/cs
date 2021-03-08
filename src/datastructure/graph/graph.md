# Graph
Graphs contains nodes and vertex. Nodes hold information while vertex represent the link they have to other nodes. 

# Implementation
1. Using a Adjacency List.
Adjacency array is basically a 2D array. This gives fast access time. Will be O(1) for insert and read. Checking if 2 nodes are connected will be O(1) as well. 
Downside would be waste of space since not all array slots are used if it's not a **full graph**

2. Using a Adjacency List. 
This is a list containing other list. The first list represent every node. Each sub-list represent the connected nodes. 
This approach will not have empty slots. 
Access time is O(1). Checking 2 nodes if connected will be O(N)

