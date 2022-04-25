import os, io, base64, urllib, uuid
import networkx as nx
import matplotlib.pyplot as plt
# from networkx.drawing.nx_agraph import graphviz_layout
from matplotlib import animation
from .algorithms import *

plt.switch_backend('agg')

def process_graph_algo(name, adj_list, heuristic=None):
	name = name.lower()
	graph_func = generate_graph
	if name == 'bfs':
		result = bfs.bfs(adj_list, list(adj_list.keys())[0])
	elif name == 'dfs':
		result = bfs.bfs(adj_list, list(adj_list.keys())[0])

	

	graph = graph_func(adj_list, result)
	return {'time_taken': 0, 'output': result, 'graph': graph}

def generate_graph(adj_list, path):
	plt.clf()
	G = nx.MultiDiGraph(adj_list)
	# nx.nx_agraph.write_dot(G,'test.dot')
	pos = nx.spring_layout(G)
	fig = plt.gcf()
	colors = ['white']*G.number_of_nodes()

	def init():
		nx.draw_networkx_nodes(G,pos,node_color=colors)
		nx.draw_networkx_edges(G, pos=pos)
		nx.draw_networkx_labels(G, pos=pos)

	def update(i):
		t = path[i]
		j = list(G.nodes).index(t)
		colors[j] = 'lightblue'
		nodes = nx.draw_networkx_nodes(G,pos,node_color=colors)
		return nodes,

	init()
	anim = animation.FuncAnimation(fig, update, frames=min(G.number_of_nodes(), len(path)), interval=1000, blit=True)
	filename = f'{uuid.uuid4()}.gif'
	anim.save(filename, writer='pillow')

	buf = io.BytesIO()
	with open(filename, 'rb') as f:
		buf.write(f.read())
	os.remove(filename)

	buf.seek(0)
	bufstr = base64.b64encode(buf.read())
	uri = urllib.parse.quote(bufstr)
	return uri