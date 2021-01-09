from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='aboutUs'),
    path('museum/<int:pk>', views.museum),
    path('test/', views.test),
    path('museums', views.museums),
    path('ajax_get_city', views.ajax_get_city),
    path('download', views.download, name='download')
]
