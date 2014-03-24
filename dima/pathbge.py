#!/usr/bin/python

'''
shortest path in unweighted graph
'''

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
	with open('pathbge1.in') as inp_file:
		first_line=inp_file.readline().strip().split()
		for lines in inp_file:
			line = lines.strip().split()
			G.add_edge(int(line[0]),int(line[1]))
	n = int(first_line[0])
	for i in range(1,n+1):
		G.add_node(i)
	def graph_path(p):
		j = 0
		lst_visited = []		#list of visited node
		current_lst = []		#list of current node
		dct_path = {}			#dict path_lenght:[node_list]
		current_level = p
		next_level = list(G.neighbor[p])		#list of next level node
		lst_visited.append(p)
		dct_path[0] = p
		while len(lst_visited) != len(G.neighbor):
			j += 1
			current_level = next_level
			next_level = []
			for item in current_level:
				if item not in lst_visited:
					current_lst.append(item)
					lst_visited.append(item)
					for items in G.neighbor[item]:
						next_level.append(items)
			dct_path[j] = current_lst
			current_lst = []
		return dct_path
	dct_path = graph_path(1)
	node_dict = {}		# Num of conn.comp:[list of node] to node: Num of conn.comp
	for key in dct_path:
		node = dct_path[key]
		if type(node) == list:
			for i in range(len(node)):
				node_dict[node[i]] = key
		else:	
			node_dict[node]=key
	out_f = open('pathbge1.out','w')
	for key in node_dict:
		out_f.write('%s '%node_dict[key])