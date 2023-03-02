from django.shortcuts import render

from source.models import Source


def index(request):
	context_dict = {}
	try:
		typing_svg_url = Source.objects.get(name="Typing SVG").url
	except:
		typing_svg_url = None

	context_dict['typing_svg_url'] = typing_svg_url
	response = render(request, 'home/index.html', context=context_dict)
	return response


def home(request):
	context_dict = {}

	response = render(request, 'home/index.html', context=context_dict)
	return response
