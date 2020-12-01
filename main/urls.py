from . import views
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('museums', views.museums),
    path('test/', views.test),
    #path('museum', views.museum)
    path('museum', views.get_comment),
    path('ajax_get_comment', views.ajax_get_comment),
    path('ajax_delete_comment', views.ajax_delete_comment)

]
