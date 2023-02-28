from django.urls import path
from django.conf.urls import include

from home import views

urlpatterns = [
	path('', views.index, name='home'),
	path('api/', include('api.urls')),
]

urlpatterns += [
	path('api-auth/', include('rest_framework.urls')),
]
