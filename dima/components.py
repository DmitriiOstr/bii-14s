#!/usr/bin/python
import sys

'''
Connected components of an undirected graph
'''

sys.setrecursionlimit(50000)

class Graph:

	'''
	idea for Graph class from http://code.activestate.com/recipes/569151-simple-graph-for-python/
	'''
	def __init__(self):
		self.node = {}
		self.neighbor = {}
	def add_node(self,node):
		self.node[node] = True
	def add_edge(self,node,nodesecond):
		try:
			self.neighbor[node].append(nodesecond)
		except:
			self.neighbor[node] = []
			self.neighbor[node].append(nodesecond)
		try:
			self.neighbor[nodesecond].append(node)
		except:
			self.neighbor[nodesecond] = []
			self.neighbor[nodesecond].append(node)
	def neighbor(self,node):
		return neighbor[node]


if __name__ == "__main__":
	G = Graph()
	with open('components.in') as inp_file:
		first_line=inp_file.readline().strip().split()
		for lines in inp_file:
			line=lines.strip().split()
			G.add_edge(int(line[0]),int(line[1]))
	n=int(first_line[0])
	for i in range(1,n+1):
		G.add_node(i)	
	lst_visited = []		#list of visited node
	lst_connections = []		#list of connected node
	dct_connections_comp = {}		# № of conn.comp:[list of node]
	def sv(p,lst_visited,lst_connections,dct_connections_comp,j):		# Depth-first search
		lst_visited.append(p)
		lst_connections.append(p)
		neib_node = G.neighbor[p]
		for node in neib_node:
			if node not in lst_visited:
				sv(node,lst_visited,lst_connections,dct_connections_comp,j)
		dct_connections_comp[j] = lst_connections
		return lst_visited,lst_connections,dct_connections_comp
	j = 1
	for p in range(1,n+1):		# Depth-first search for all node
		if p not in lst_visited and p in list(G.neighbor):
			lst_connections = []
			sv(p,lst_visited,lst_connections,dct_connections_comp,j)
			j += 1
		elif p not in lst_visited and p not in list(G.neighbor):
			dct_connections_comp[j] = [p]
			j += 1
	node_dict = {}		# № of conn.comp:[list of node] to node: № of conn.comp
	for key in dct_connections_comp:
		node = dct_connections_comp[key]
		if type(node) == list:
			for i in range(len(node)):
				node_dict[node[i]] = key
		else:	
			node_dict[node]=key
	out_f = open('components.out','w')
	out_f.write('%s\n'%len(dct_connections_comp))
	for key in node_dict:
		out_f.write('%s '%node_dict[key])