from . import views
from django.urls import path
from comment.views import Comment

urlpatterns = [

    path('', views.index, name='index'),
    path('museum/<int:pk>', views.museum),
    # path(r'^(museums/(?P<pk>\d+))/$', views.museum),
    path('test/', views.test),
    path('museums', views.museums),

]
