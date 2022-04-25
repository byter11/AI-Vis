from django import forms

class GraphForm(forms.Form):
	template_name = 'form_snippet.html'
	graph = forms.CharField(label="", widget=forms.Textarea(attrs={'placeholder': 'Adjacency List:\nExample:\na:b,c\nb:c'}))

class GeneticAlgorithmForm(forms.Form):
	template_name = 'form_snippet.html'
	target = forms.CharField(label="Target")
	n_pop = forms.IntegerField(label="Population size")
	cross_rate = forms.FloatField(label="Crossover rate", widget=forms.NumberInput(attrs={'step': 0.05}))
	mutations_per_ch = forms.FloatField(label="Mutation rate", widget=forms.NumberInput(attrs={'step': 0.05}))