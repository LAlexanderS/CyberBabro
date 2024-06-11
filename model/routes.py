import networkx as nx

class Routes:
	def __init__(self, vertexes):
		self.graph = nx.Graph()
		#self.graph.add_nodes_from(vertexes)
		for record in vertexes:
			record['time'] = record['time'].replace(',', '.')
			if 'id_st1' in record:
				self.graph.add_edge(int(record['id_st1']), int(record['id_st2']), weight=float(record['time']))
			else:
				self.graph.add_edge(int(record['id1']), int(record['id2']), weight=float(record['time']))

	def GetGraph(self):
		return self.graph
	
	def CalcDistance(self, source, destination):
		try:
			path = nx.shortest_path(self.graph, source=source, target=destination)
			distance = nx.shortest_path_length(self.graph, source=source, target=destination)
			return path, distance
		except nx.NetworkXNoPath:
			return None, float('inf')