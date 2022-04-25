import datetime
from .algorithms.genetic import genetic_algorithm
import matplotlib.pyplot as plt
from matplotlib import animation
from base.src.util import anim_to_bytes

import numpy as np
plt.switch_backend('agg')

def process_ml_algo(name, input):
	name = name.lower()
	start = datetime.datetime.now()
	if name == 'genetic-algorithm':
		gens, best, found, fitness = genetic_algorithm(**input)
	
	time_taken = (datetime.datetime.now() - start).microseconds
	graph = generate_graph(fitness)
	return {
		'output': {'time_taken': f'{time_taken}ms', 'gens': gens, 'best': best, 'found': found}, 
		'graph': graph
	}

def generate_graph(fitness):
	plt.clf()
	gens = len(fitness)
	data = [f[1] for f in fitness]
	m = np.array(data)
	pop = m[0].size

	y = m.reshape(-1)
	x = np.repeat(range(gens), pop)
	
	step = int(max(1, y.size/15 + 1))
	def init():
		plt.scatter(x[:step], y[:step], s=1)
		plt.xlim(0, len(fitness))
		plt.xlabel('Generation #')
		plt.ylabel('Fitness')
		plt.title(fitness[0][0])
	
	def update(i):
		k = i*step
		for j in range(k, k+step, pop):
			plt.scatter(x[j:j+pop], y[j:j+pop], s=1)
		plt.title(fitness[x[k+step]][0])

	fig = plt.gcf()
	init()
	anim = animation.FuncAnimation(fig, update, frames=14, interval=1, blit=False)
	return anim_to_bytes(anim)
