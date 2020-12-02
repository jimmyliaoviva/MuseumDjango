from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('museum/<int:pk>', views.museum),
    path('test/', views.test),
    path('museums', views.museums),
]
