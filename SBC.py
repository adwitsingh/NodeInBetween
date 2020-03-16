# CSE 101 - IP HW3
# Betweenness Centrality 
# Name: ADWIT SINGH KOCHAR
# Roll Number: 2018276
# Section: B
# Group: 5
import re
import itertools
from copy import deepcopy

ROLLNUM_REGEX = "201[0-9]{4}"

class Graph(object):
	name = "ADWIT SINGH KOCHAR"
	email = "adwit18276@iiitd.ac.in"
	roll_num = "2018276"

	def __init__ (self, vertices, edges):
		"""
		Initializes object for the class Graph

		Args:
			vertices: List of integers specifying vertices in graph
			edges: List of 2-tuples specifying edges in graph
		"""

		self.vertices = vertices
		
		self.dictVertices = {x:[False, -1] for x in vertices}					# Dictionary with elements as:
																				#	{ Node:[ Visited? , Distance from start_node ] }
		ordered_edges = list(map(lambda x: (min(x), max(x)), edges))
		self.edges    = ordered_edges
		
		self.adjacent={}
		for i in self.vertices:													# Dictionary with vertices as keys having value
			self.adjacent[i]=[]													# as a list of adjacent nodes
			for j in self.edges:
				if i in j:
					self.adjacent[i].append(j[0] if j[0]!=i else j[1])

		self.validate()

	def validate(self):
		"""
		Validates if Graph if valid or not

		Raises:
			Exception if:
				- Name is empty or not a string
				- Email is empty or not a string
				- Roll Number is not in correct format
				- vertices contains duplicates
				- edges contain duplicates
				- any endpoint of an edge is not in vertices
		"""

		if (not isinstance(self.name, str)) or self.name == "":
			raise Exception("Name can't be empty")

		if (not isinstance(self.email, str)) or self.email == "":
			raise Exception("Email can't be empty")

		if (not isinstance(self.roll_num, str)) or (not re.match(ROLLNUM_REGEX, self.roll_num)):
			raise Exception("Invalid roll number, roll number must be a string of form 201XXXX. Provided roll number: {}".format(self.roll_num))

		if not all([isinstance(node, int) for node in self.vertices]):
			raise Exception("All vertices should be integers")

		elif len(self.vertices) != len(set(self.vertices)):
			duplicate_vertices = set([node for node in self.vertices if self.vertices.count(node) > 1])

			raise Exception("Vertices contain duplicates.\nVertices: {}\nDuplicate vertices: {}".format(vertices, duplicate_vertices))

		edge_vertices = list(set(itertools.chain(*self.edges)))

		if not all([node in self.vertices for node in edge_vertices]):
			raise Exception("All endpoints of edges must belong in vertices")

		if len(self.edges) != len(set(self.edges)):
			duplicate_edges = set([edge for edge in self.edges if self.edges.count(edge) > 1])

			raise Exception("Edges contain duplicates.\nEdges: {}\nDuplicate vertices: {}".format(edges, duplicate_edges))

	def min_dist(self, start_node, end_node):
		'''
		Finds minimum distance between start_node and end_node

		Args:
			start_node: Vertex to find distance from
			end_node: Vertex to find distance to

		Returns:
			An integer denoting minimum distance between start_node
			and end_node
		'''
		vertex_bio = deepcopy(self.dictVertices)							# Stores details of visited vertices and their distance
		vertex_bio[start_node][0]=True										# - from start_node.
		vertex_bio[start_node][1]=0

		queue=[]															# \
		queue.append(start_node)											#  |		
																			#  |
		while (len(queue)!=0):												#  |
			popped_vertex=queue.pop(0)										#   \	Breadth First Search
			for i in self.adjacent[popped_vertex]:							#   /		Implementation
				if vertex_bio[i][0] == False:								#  |
					vertex_bio[i][0] = True									#  |
					vertex_bio[i][1] = vertex_bio[popped_vertex][1]+1		#  |
					queue.append(i)											# /

		return(vertex_bio[end_node][1])


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
		allPaths = []
		visited.append(node)												# Adds current node to list of previous visited nodes

		if node == destination:												# If destination reached, 
			allPaths.append([destination])									# - append destination and
			return allPaths 												# - return back to last cross road.
		
		else:
			for i in self.adjacent[node]:
				
				if i not in visited:										# Prevents traceback 
					copy_visited = deepcopy(visited)
					next_nodes = self.all_paths(i, destination, copy_visited, -1)
					if next_nodes:
						allPaths.extend(next_nodes)
		
		for i in allPaths:
			i.insert(0, node)												# Appends the starting node before and node in list.

		if dist != -1:														# Runs only in the outermost function and not in recursive calls
			desiredPaths = []
			for i in allPaths:
				if len(i)==dist+1:
					desiredPaths.append(i)									# Out of all paths, picks paths of required length.
			return desiredPaths
		else:
			return allPaths

	def all_shortest_paths(self, start_node, end_node):
		"""
		Finds all shortest paths between start_node and end_node

		Args:
			start_node: Starting node for paths
			end_node: Destination node for paths

		Returns:
			A list of path, where each path is a list of integers.
		"""
		min_dist = self.min_dist(start_node, end_node)						# Finds minimum distance b/w start_node and end_node 

		shortestPaths = self.all_paths(start_node, end_node, [], min_dist)	# Retrieves all paths b/w start_node and end_node of minimum length

		return shortestPaths
		
	

	def betweenness_centrality(self, node):
		"""
		Find betweenness centrality of the given node

		Args:
			node: Node to find betweenness centrality of.

		Returns:
			Single floating point number, denoting betweenness centrality
			of the given node
		"""
		BtwCent = 0
		notNode=deepcopy(self.vertices)											# List of all nodes except node in focus.
		notNode.remove(node)
		
		for i in range(len(notNode)):
			for j in range(i+1,len(notNode)):
				shortPaths = self.all_shortest_paths(notNode[i], notNode[j])	# Takes all possible pairs of nodes
				
				allShortPaths = len(shortPaths)									# Total no. of shortest paths b/w nodes
				
				shortPathsThroughNode = 0
				for x in shortPaths:
					if node in x:
						shortPathsThroughNode+=1								# Collects paths that pass through node in focus 
				
				BtwCent += (shortPathsThroughNode/allShortPaths)				# Betweenness Centrality formula

		return BtwCent


	def top_k_betweenness_centrality(self):
		"""
		Find top k nodes based on highest equal standard betweenness centrality.
		
		Returns:
			List a integer, denoting top k nodes based on standard betweenness
			centrality.
		"""
		n = len(self.vertices)
		
		standardFactor = 2/((n-1)*(n-2))										# Factor that when multiplied with B.C. gives Standard B.C.

		BtwCentList = []
		for i in self.vertices:
			standardBtwCent = self.betweenness_centrality(i)*standardFactor
			BtwCentList.append([i, standardBtwCent])							# Creates a list of all nodes with their Standard Betweeness Centrality.
			
		BtwCentList.sort(key=lambda x: x[1], reverse=True)						# Sorts nodes according to their S.B.C. in descending order.
		
		print("Node(s) having top Betweenness Centrality (",BtwCentList[0][1],") = ", end="")
		for i in BtwCentList:
			if i[1] == BtwCentList[0][1]:										# If S.B.C of node is equal to maximum S.B.C found,
				print(i[0], end=" ")											# - print node.
		print()
		

if __name__ == "__main__":
	import ast

	print("Enter list of vertices: ", end="")
	vertices = input()
	vertices = ast.literal_eval(vertices)

	print("Enter list of edges: ", end="")
	edges = input()
	edges = ast.literal_eval(edges)

	graph = Graph(vertices, edges)
	graph.top_k_betweenness_centrality()

	
