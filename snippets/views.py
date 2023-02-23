from django.shortcuts import render
from django.http import HttpResponse, JsonResponse # JsonResponse is used to return JSON data
from django.views.decorators.csrf import csrf_exempt # csrf_exempt is used to allow POST requests from clients that won't have a CSRF token
from rest_framework.parsers import JSONParser # JSONParser is used to parse JSON data
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


# List all code snippets, or create a new snippet.
@csrf_exempt
def snippet_list(request):
	if request.method == 'GET':
		snippets = Snippet.objects.all()
		serializer = SnippetSerializer(snippets, many=True)
		return JsonResponse(serializer.data, safe=False)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = SnippetSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)


# Retrieve, update or delete a code snippet.
@csrf_exempt
def snippet_detail(request, pk):
	try:
		snippet = Snippet.objects.get(pk=pk)
	except Snippet.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = SnippetSerializer(snippet)
		return JsonResponse(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = SnippetSerializer(snippet, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		snippet.delete()
		return HttpResponse(status=204)
