from django.shortcuts import render
import django.contrib.auth as auth
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


# Create your views here.

def login(request):
    try:
        redirect_to = request.GET["next"]
    except:
        redirect_to = "/"
    if request.user.is_authenticated:
        return HttpResponseRedirect('/index/')
    username = request.POST.get('InputEmail', '')
    password = request.POST.get('InputPassword', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect(redirect_to)
    else:
        return HttpResponseRedirect(redirect_to)


def logout(request):
    try:
        redirect_to = request.GET["next"]
    except:
        redirect_to = "/"
    auth.logout(request)
    return HttpResponseRedirect(redirect_to)


def register(request):
    try:
        redirect_to = request.GET["next"]
    except:
        redirect_to = "/"
    email = request.POST.get('InputEmail')
    username = request.POST.get('InputName', '')
    password = request.POST.get('InputPassword', '')
    auth.models.User.objects.create_user(username, email, password)
    user = auth.authenticate(username=username, password=password)
    auth.login(request, user)
    return HttpResponseRedirect(redirect_to)
