from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views

urlpatterns = format_suffix_patterns([
    	# function based views
	# path('snippets/', views.snippet_list),
	# path('snippets/<int:pk>/', views.snippet_detail),
	path('', views.api_root),

	# class based mixin views
	# path('snippets/', views.SnippetListMixin.as_view()),
	# path('snippets/<int:pk>/', views.SnippetDetailMixin.as_view()),
	
	# class based generic views
	path('users/', views.UserList.as_view(), name='user-list'),
	path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
	path('snippets/', views.SnippetListGeneric.as_view(), name='snippet-list'),
	path('snippets/<int:pk>/', views.SnippetDetailGeneric.as_view(), name='snippet-detail'),
	path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),
])
