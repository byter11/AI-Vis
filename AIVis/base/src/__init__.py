from base.src import bfs
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import animation

def process_graph_algo(name, adj_list):
	if name.lower() == 'bfs':
		result = bfs.bfs(adj_list, list(adj_list.keys())[0])
		graph = generate_graph(adj_list, result)
		return {'time_taken': 0, 'output': result}

def generate_graph(adj_list, path):
	G = nx.Graph(adj_list)

	colors = ['white']*G.number_of_nodes()
	pos = nx.spring_layout(G)
	nodes = nx.draw_networkx_nodes(G,pos,node_color=colors)
	edges = nx.draw_networkx_edges(G, pos=pos)
	labels = nx.draw_networkx_labels(G, pos=pos)

	def update(i):
		t = path[i]
		colors[i] = 'lightblue'
		nodes = nx.draw_networkx_nodes(G,pos,node_color=colors)
		return nodes,

	fig = plt.gcf()
	anim = animation.FuncAnimation(fig, update, frames=G.number_of_nodes(), interval=1000, blit=True)
	anim.save('crap.gif', writer='imagemagick')