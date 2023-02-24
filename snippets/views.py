from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt # csrf_exempt is used to exempt a view from CSRF protection

from rest_framework import status # status is used to return HTTP status codes
from rest_framework.decorators import api_view # api_view is used to wrap API views
from rest_framework.response import Response # Response is used to return a Response object

from snippets.models import Snippet # Import the Snippet model
from snippets.serializers import SnippetSerializer # Import the SnippetSerializer


@csrf_exempt
# Type of request that the view will accept
@api_view(['GET', 'POST'])
# List all code snippets, or create a new snippet
def snippet_list(request, format=None):
	if request.method == 'GET':
		snippets = Snippet.objects.all()
		serializer = SnippetSerializer(snippets, many=True)

		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = SnippetSerializer(data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, stats = status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
# Retrieve, update or delete a code snippet
def snippet_detail(request, pk, format=None):
	try:
		snippet = Snippet.objects.get(pk=pk)
	except Snippet.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = SnippetSerializer(snippet)

		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = SnippetSerializer(snippet, data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		snippet.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
