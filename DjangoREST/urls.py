from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.conf.urls import include
from django.contrib import admin

from home import views

admin.site.site_header = "Admin"
admin.site.site_title = "Admin"
admin.site.index_title = "Admin"

urlpatterns = [
	path('', views.index, name='home'),
	path('api/', include('api.urls')),
    	path('admin/', admin.site.urls),
      path('home/', include('home.urls')),
      path('resume/', views.resume, name='resume'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
	path('api-auth/', include('rest_framework.urls')),
]
