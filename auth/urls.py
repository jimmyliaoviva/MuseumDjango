from . import views
from django.urls import path

urlpatterns = [
    path('accounts/login', views.login, name='login'),
    path('accounts/logout', views.logout, name='logout'),
    path('accounts/register', views.register, name="register")
]
