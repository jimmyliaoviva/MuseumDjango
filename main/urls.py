from . import views
from django.urls import path
from comment.views import Comment
urlpatterns = [
    path('', views.index, name='index'),
    path('museums/<int:pk>', views.museum),
    path('test/', views.test),
    path('museum', views.museums),

]
