from django_filters.rest_framework import FilterSet

from rest_framework import permissions
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response

from api.permissions import IsAuthorOrReadOnly
from api.serializers import SymbolSerializer, SymbolDetailSerializer, UnitSerializer, UnitDetailSerializer, SystemSerializer, SystemDetailSerializer

from unit.models import Symbol, Unit, System


class ApiRoot(generics.GenericAPIView):
	name = 'API Root'

	def get(self, request, *args, **kwargs):
		return Response({
			'symbols': reverse('api:symbol-list', request=request),
			'units': reverse('api:unit-list', request=request),
			'systems': reverse('api:system-list', request=request),
		})


class SymbolFilter(FilterSet):
	class Meta:
		model = Symbol
		fields = ('symbol', )


class SymbolList(generics.ListCreateAPIView):
	queryset = Symbol.objects.all()
	serializer_class = SymbolSerializer
	name = 'Symbol List'
	pagination_class = None
	search_fields = ('^symbol',)
	ordering_fields = ('symbol',)
	filter_class = SymbolFilter
	permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

	def perform_create(self, serializer):
		serializer.save(author=self.request.user)


class SymbolDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Symbol.objects.all()
	serializer_class = SymbolDetailSerializer
	name = 'Symbol Detail'
	lookup_field = 'symbol'
	search_fields = ('^symbol',)
	ordering_fields = ('symbol',)
	filter_class = SymbolFilter
	permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly,]

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)


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
	lookup_field = 'name'
	search_fields = ('^name',)
	ordering_fields = ('name',)
	filter_class = UnitFilter
	permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly,]

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)


class SystemFilter(FilterSet):
	class Meta:
		model = System
		fields = ('name', )


class SystemList(generics.ListCreateAPIView):
	queryset = System.objects.all()
	serializer_class = SystemSerializer
	name = 'System List'
	pagination_class = None
	search_fields = ('^name',)
	ordering_fields = ('name',)
	filter_class = SystemFilter
	permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

	def perform_create(self, serializer):
		serializer.save(author=self.request.user)


class SystemDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = System.objects.all()
	serializer_class = SystemDetailSerializer
	name = 'System Detail'
	lookup_field = 'name'
	search_fields = ('^name',)
	ordering_fields = ('name',)
	filter_class = SystemFilter
	permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly,]

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
