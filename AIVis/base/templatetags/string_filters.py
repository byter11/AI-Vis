from django import template

register = template.Library()

@register.filter(name="hyphenize")
def hyphenize(value):
	return value.replace(' ', '-')

@register.filter(name="unhyphenize")
def unhyphenize(value):
	return value.replace('-', ' ')

@register.filter(name="lower")
def lower(value):
	return value.lower()

