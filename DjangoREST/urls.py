from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.conf.urls import include

from home import views

urlpatterns = [
	path('', views.index, name='home'),
	path('api/', include('api.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
	path('api-auth/', include('rest_framework.urls')),
]
