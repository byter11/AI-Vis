from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from base.forms import GraphForm, GeneticAlgorithmForm
from base.src import process_graph_algo, process_ml_algo

# Create your views here.
def get_algorithm(request, option='BFS'):
	algorithms = [
		('Uninformed Search', ['BFS', 'DFS']),
		('Machine Learning', ['Genetic Algorithm'])
	]
	graph_algos = ['bfs', 'dfs', 'ucs']

	input_method = ''
	form = None
	result = None

	if option in graph_algos:
		input_method = 'graph'
		form = GraphForm(request.POST or None, initial={'graph': 'a:b'})
		if form.is_valid():
			graph = form.cleaned_data['graph']
		else:
			graph = 'a:b'
		adj_list = {}
		for line in graph.split('\n'):
			node, edges = line.strip().split(':')
			adj_list[node] = edges.strip().split(',')
		result = process_graph_algo(option, adj_list)
	
	elif option in ['genetic-algorithm']:
		input_method = 'genetic'
		initial = {
			'target': 'Algorithm',
			'n_pop': 50,
			'cross_rate': 0.9,
			'mutations_per_ch': 2
		}
		form = GeneticAlgorithmForm(request.POST or None, initial=initial)
		if form.is_valid():
			data = form.cleaned_data
		else:
			data = initial
		result = process_ml_algo(option, data)

	if result:
		result['output'] = '\n'.join([f"{k}: {v}" for k, v in result['output'].items()])
	return render(request, 'index.html', {
		'algorithms': algorithms, 
		'input': input_method, 
		'option': option,
		'form': form,
		'result': result
	})
