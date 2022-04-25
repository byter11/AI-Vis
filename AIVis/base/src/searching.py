import os, io, base64, urllib, uuid, datetime
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import animation
from .algorithms import bfs, dfs

plt.switch_backend('agg')

def process_graph_algo(name, adj_list, heuristic=None):
	graph_func = generate_graph

	start = datetime.datetime.now()
	if name == 'bfs':
		result = bfs.bfs(adj_list, list(adj_list.keys())[0])
	elif name == 'dfs':
		result = dfs.dfs(adj_list, list(adj_list.keys())[0])
	time_taken = (datetime.datetime.now() - start).microseconds
	

	graph = graph_func(adj_list, result)
	return {
		'output': {'time_taken': f'{time_taken}ms', 'path': ', '.join(result)}, 
		'graph': graph
	}

def generate_graph(adj_list, path):
	plt.clf()
	G = nx.MultiDiGraph(adj_list)
	pos = nx.random_layout(G)
	fig, axe = plt.subplots(figsize=(5,3))	
	colors = ['white']*G.number_of_nodes()

	def init():
		nx.draw_networkx_nodes(G,pos,node_color=colors)
		nx.draw_networkx_edges(G, pos=pos)
		nx.draw_networkx_labels(G, pos=pos)

	def update(i):
		t = path[i]
		plt.title(', '.join(path[:i+1]), loc='left')
		j = list(G.nodes).index(t)
		colors[j] = 'orange'
		nodes = nx.draw_networkx_nodes(G,pos,node_color=colors)
		return nodes,

	init()
	plt.title(', '.join(path), loc='left')
	plt.tight_layout()
	anim = animation.FuncAnimation(fig, update, frames=min(G.number_of_nodes(), len(path)), interval=1000, blit=False)
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