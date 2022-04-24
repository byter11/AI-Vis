from django import forms

class GraphForm(forms.Form):
	template_name = 'form_snippet.html'
	graph = forms.CharField(label="", widget=forms.Textarea(attrs={'placeholder': 'Adjacency List:\nExample:\na:b,c\nb:c'}))