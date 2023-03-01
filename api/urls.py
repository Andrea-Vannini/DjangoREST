from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views


app_name = 'api'
urlpatterns = [
	path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),

	path('symbols/', views.SymbolList.as_view(), name='symbol-list'),
	path('symbols/<symbol>', views.SymbolDetail.as_view(), name='symbol-detail'),
	path('units/', views.UnitList.as_view(), name='unit-list'),
	path('units/<name>', views.UnitDetail.as_view(), name='unit-detail'),
	path('systems/', views.SystemList.as_view(), name='system-list'),
	path('systems/<name>', views.SystemDetail.as_view(), name='system-detail'),
    
	path('origins/', views.OriginList.as_view(), name='origin-list'),
	path('origins/<int:pk>', views.OriginDetail.as_view(), name='origin-detail'),
	path('sources/', views.SourceList.as_view(), name='source-list'),
	path('sources/<int:pk>', views.SourceDetail.as_view(), name='source-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
