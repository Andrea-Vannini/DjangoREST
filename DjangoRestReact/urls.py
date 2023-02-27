from django.urls import path
from django.conf.urls import include

urlpatterns = [
	path('api/', include('api.urls')),
]

urlpatterns += [
    	path('api-auth/', include('rest_framework.urls')),
]
