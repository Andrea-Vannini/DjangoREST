from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
	# function based views
	path('snippets/', views.snippet_list),
	path('snippets/<int:pk>/', views.snippet_detail),

	# class based mixin views
	path('snippets_mixin/', views.SnippetListMixin.as_view()),
	path('snippets_mixin/<int:pk>/', views.SnippetDetailMixin.as_view()),
	
	# class based generic views
	path('snippets_generic/', views.SnippetListGeneric.as_view()),
	path('snippets_generic/<int:pk>/', views.SnippetDetailGeneric.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
