from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views


app_name = 'api'
urlpatterns = [
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),

    path('units/', views.UnitList.as_view(), name='unit-list'),
    path('units/<int:pk>', views.UnitDetail.as_view(), name='unit-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
