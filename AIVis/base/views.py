from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from base.forms import GraphForm
from base.src import process_graph_algo

# Create your views here.
def get_algorithm(request, option='BFS'):
	algorithms = [
		('Uninformed Search', ['BFS', 'DFS'])
	]
	graph_algos = ['BFS', 'DFS', 'UCS']

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

	return render(request, 'index.html', {
		'algorithms': algorithms, 
		'input': input_method, 
		'option': option,
		'form': form,
		'result': result
	})
