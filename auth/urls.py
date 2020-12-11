from . import views
from django.urls import path

urlpatterns = [
    path('accounts/login', views.login, name='login'),
    path('accounts/logout', views.logout, name='logout'),
    path('accounts/register', views.register, name="register"),
    path('edit_name', views.edit_name, name='edit_name'),
    path('edit_pass', views.edit_pass, name='edit_pass'),
    path('edit_all', views.edit_all, name='edit_all'),
]
