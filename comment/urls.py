from . import views
from django.urls import path

from django.contrib import admin

urlpatterns = [
    path('ajax_add_comment', views.ajax_add_comment),
    path('ajax_get_comment', views.ajax_get_comment),
    path('ajax_delete_comment', views.ajax_delete_comment),
]
