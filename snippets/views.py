from django.shortcuts import render # Return a HttpResponse whose content is filled with the result of calling django.template.loader.render_to_string() with the passed arguments
from django.views.decorators.csrf import csrf_exempt # csrf_exempt is used to exempt a view from CSRF protection
from django.contrib.auth.models import User

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter

from rest_framework import mixins, generics, permissions
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND # same as status.HTTP_code, but for specific status codes for simplicitys sake
from rest_framework.decorators import api_view # api_view is used to wrap API views
from rest_framework.response import Response # Response is used to return a Response object
from rest_framework.reverse import reverse # reverse is used to return a fully-qualified URL given a view name and optional parameters
from rest_framework import renderers # renderers is used to renderers for HTML and Browsable API

from snippets.models import Snippet
from snippets.permissions import IsOwnerOrReadOnly
from snippets.serializers import UserSerializer, SnippetSerializer


@api_view(['GET'])
def api_root(request, format=None):
	return Response({
		'users': reverse('user-list', request=request, format=format),
		'snippets': reverse('snippet-list', request=request, format=format)
	})


class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


@csrf_exempt
# Type of request that the view will accept
@api_view(['GET', 'POST'])
# List all code snippets, or create a new snippet with function based view
def snippet_list(request, format=None):
	if request.method == 'GET':
		snippets = Snippet.objects.all()
		serializer = SnippetSerializer(snippets, many=True)

		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = SnippetSerializer(data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=HTTP_201_CREATED)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


# List all snippets, or create a new snippet with class based view and mixins
class SnippetListMixin(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)


# List all snippets, or create a new snippet with class based view and generics
class SnippetListGeneric(generics.ListCreateAPIView):
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
# Retrieve, update or delete a code snippet with function based view
def snippet_detail(request, pk, format=None):
	try:
		snippet = Snippet.objects.get(pk=pk)
	except Snippet.DoesNotExist:
		return Response(status=HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = SnippetSerializer(snippet)

		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = SnippetSerializer(snippet, data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		snippet.delete()
		return Response(status=HTTP_204_NO_CONTENT)


# Retrieve, update or delete a code snippet with class based view and mixins
class SnippetDetailMixin(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer

	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)


# Retrieve, update or delete a code snippet with class based view and generics
class SnippetDetailGeneric(generics.RetrieveUpdateDestroyAPIView):
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class SnippetHighlight(generics.GenericAPIView):
	queryset = Snippet.objects.all()
	renderer_classes = [renderers.StaticHTMLRenderer]

	def get(self, request, *args, **kwargs):
		snippet = self.get_object()
		return Response(snippet.highlighted)
