# NodeInBetween
Python application which returns all the nodes with highest Betweenness Centrality in a given undirected unweighted graph.

Betweenness centrality finds wide application in network theory apart from biology, transport and scientific cooperation: it represents the degree of which nodes stand between each other. For example, in a network, a node with higher betweenness centrality would have more control over the network, because more information will pass through that node. This is used extensively in social media analysis.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

This project needs python3 installed on the local machine along with *re*, *itertools* and *ast*, which can be installed using:

```bash
$ python3 -m pip install ast
$ python3 -m pip install re
$ python3 -m pip install itertools
```



### Executing

SBC.py defines a class **Graph** which takes *vertices* and *edges* as arguments:

##### 		vertices: List of integers as vertices in the given graph.

##### 		edges: List of 2-element tuple as edges in the given graph.

The following methods are defined in the module:

1. ```python
   def min_dist(self, start_node, end_node):
   		"""
   		Finds minimum distance between start_node and end_node
   
   		Args:
   			start_node: Vertex to find distance from
   			end_node: Vertex to find distance to
   
   		Returns:
   			An integer denoting minimum distance between start_node
   			and end_node
   		"""
   ```

2. ```python
   def all_paths(self, node, destination, visited, dist):
   		"""
   		Finds all paths from node to destination with length = dist
   
   		Args:
   			node: Node to find path from
   			destination: Node to reach
   			visited: Nodes already visited. Prevents traceback in recursion
   			dist: Allowed distance of path
   		   
   		Returns:
   			List of path, where each path is list ending on destination
   
   			Returns None if there no paths
   		"""
   ```

3. ```python
   def all_shortest_paths(self, start_node, end_node):
   		"""
   		Finds all shortest paths between start_node and end_node
   
   		Args:
   			start_node: Starting node for paths
   			end_node: Destination node for paths
   
   		Returns:
   			A list of path, where each path is a list of integers.
   		"""
   ```

4. ```python
   def betweenness_centrality(self, node):
   		"""
   		Find betweenness centrality of the given node
   
   		Args:
   			node: Node to find betweenness centrality of.
   
   		Returns:
   			Single floating point number, denoting betweenness centrality
   			of the given node
   		"""
   ```

5. ```python
   def top_k_betweenness_centrality(self):
   		"""
   		Find top k nodes based on highest equal standard betweenness 				centrality.
   		
   		Returns:
   			List a integer, denoting top k nodes based on standard 						betweenness centrality.
   		"""
   ```

To run the module:

```bash
$ python3 SBC.py
```



## Example

```bash
$ python3 SBC.py 
Enter list of vertices: [0,1,2,3,4]
Enter list of edges: [(0,1), (1,4), (1,2), (1,3), (3,4)]
Node(s) having top Betweenness Centrality ( 0.8333333333333333 ) = 1
```



## Authors

* **Adwit Singh Kochar** - *Initial work* - [adwitsingh](https://github.com/adwitsingh)
