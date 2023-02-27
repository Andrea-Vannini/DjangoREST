from django_filters.rest_framework import FilterSet

from rest_framework import permissions
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response

from api.serializers import UnitSerializer, UnitDetailSerializer
from api.permissions import IsAuthorOrReadOnly

from unit.models import Unit


class ApiRoot(generics.GenericAPIView):
	name = 'API Root'

	def get(self, request, *args, **kwargs):
		return Response({
			'units': reverse('api:unit-list', request=request),
		})


class UnitFilter(FilterSet):
	class Meta:
		model = Unit
		fields = ('name', )


class UnitList(generics.ListCreateAPIView):
	queryset = Unit.objects.all()
	serializer_class = UnitSerializer
	name = 'Unit List'
	pagination_class = None
	search_fields = ('^name',)
	ordering_fields = ('name',)
	filter_class = UnitFilter
	permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

	def perform_create(self, serializer):
		serializer.save(author=self.request.user)

class UnitDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Unit.objects.all()
	serializer_class = UnitDetailSerializer
	name = 'Unit Detail'
	lookup_field = 'pk'
	search_fields = ('^name',)
	ordering_fields = ('name',)
	filter_class = UnitFilter
	permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly,]

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
