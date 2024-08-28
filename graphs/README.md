# Graphs

## Basics

Graph consists of a finite set of vertices (nodes) and set of edges between the vertices (undirected/directed edges). Edges can be defined using an edge list or an adjacency matrix.

The Adjacency matrix of an undirected graph is symmetric in nature, whereas it is not for a directed graph.&#x20;

Adjacency matrices are easier to follow and represent, and look up, insertion, and deletion can be done in O(1) constant time. However it takes up O(V^2) space, which does not make sense if the graph is sparse

Adjacency list is an array of linked list that represents the graph. TC:\
\- Retrieving the neighbors of a vertex: O(1)\
\- Find specifc edge (x,y): O(d) where d = degree of vertex

Maximum value for degree d = |V| - 1 (edges to all vertices except itself)\
Minimum value = 0 (isolated vertex)

Reference: [https://medium.com/basecs/from-theory-to-practice-representing-graphs-cfd782c5be38](https://medium.com/basecs/from-theory-to-practice-representing-graphs-cfd782c5be38)

## BFS Traversal

### Key attributes

* BFS traverses the graph level-wise
* Time complexity: O(V+E)
  * We iterate over each node's adjacency list once. Thus we visit V nodes (V time O(1) deque operation) and E edges (2E in case of undirected edges), thus making the TC O(V+E)
* It can help determine the shortest path of an unweighted graph
  * We can backtrack from the end node's parent and so on, until we reach the staring node. This is one of the shortest path, which is equivalent to the level of the end node.
* Graph traversal can begin anywhere as there's no concept of a root node

### Steps

1. Add a node/vertex from the graph to a queue of nodes to be “visited”.
2. Visit the topmost node in the queue, and mark it as such.
3. If that node has any neighbors, check to see if they have been “visited” or not.
4. Add any neighboring nodes that still need to be “visited” to the queue.
5. Remove the node we’ve visited from the queue.

{% code overflow="wrap" %}
```python
from collections import deque
def graph_bfs_traversal(adj_list, start_node):
    queue = deque()
    queue.append(start_node)
    visited = [0]*len(adj_list)
    visited[start_node] = 1
    prev = [None]*len(adj_list)
    bfs_traversal = []

    while queue:
        node = queue.popleft() #O(1) operation
        bfs_traversal.append(node)
        neighbors = adj_list[node]

        for neighbor in neighbors:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                prev[neighbor] = node
            
    return bfs_traversal, prev
    
def get_path(start_node, end_node, prev):
    path = [end_node]
    while end_node:
        end_node = prev[end_node]
        path.append(end_node)
    
    if path[-1] != start_node:
        return []
    return path[::-1]
         
def addEdge(adjList, u, v):
    adjList[u].append(v)

# Number of vertices in the graph
vertices = 5
adjList = [[] for _ in range(vertices)]

# Add edges to the graph
addEdge(adjList, 0, 1)
addEdge(adjList, 0, 2)
addEdge(adjList, 1, 3)
addEdge(adjList, 1, 4)
addEdge(adjList, 2, 4)

print(adjList)

# Perform BFS traversal starting from vertex 0
print("Breadth First Traversal starting from vertex 0:", end=" ")
bfs_traversal, prev = graph_bfs_traversal(adjList, 0)
print("traversal: ", bfs_traversal)
print("prev: ", prev)

print(get_path(0, 2, prev))
```
{% endcode %}

## DFS Traversal

{% code overflow="wrap" %}
```python
def graph_dfs_traversal(adj_list, start_node, visited, traversal):

    if not visited[start_node]:
        neighbors = adj_list[start_node]
        visited[start_node] = True
        traversal.append(start_node)
        for neighbor in neighbors:
            graph_dfs_traversal(adj_list, neighbor, visited, traversal)
    
    return

def count_connected_components(adj_list, visited):
    count = 0
    components = []

    for node in range(len(adj_list)):
        if not visited[node]:
            count += 1
            traversal = []
            graph_dfs_traversal(adj_list, node, visited, traversal)
            components.append(traversal)
            
    return count, components
            
            
def addEdge(adjList, u, v):
    adjList[u].append(v)
# Number of vertices in the graph
vertices = 5
adjList = [[] for _ in range(vertices)]

# Add edges to the graph
addEdge(adjList, 0, 1)
addEdge(adjList, 0, 2)
addEdge(adjList, 1, 3)
# addEdge(adjList, 1, 4)
# addEdge(adjList, 2, 4)


print(adjList)

# Perform BFS traversal starting from vertex 0
visited = [False]*vertices
traversal = []

graph_dfs_traversal(adjList, 0, visited, traversal)
print("Depth First Traversal starting from vertex 0:", end=" ")
print(traversal)

# run the connected components experiment
visited = [False]*vertices
count, components = count_connected_components(adjList, visited)

print("Number of connected components", count)
print("All connected components", components)
```
{% endcode %}
