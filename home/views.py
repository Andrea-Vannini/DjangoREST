from django.shortcuts import render


def index(request):
	context_dict = {}

	response = render(request, 'home/index.html', context=context_dict)
	return response


def home(request):
	context_dict = {}

	response = render(request, 'home/index.html', context=context_dict)
	return response
