from django.shortcuts import render
import django.contrib.auth as auth
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


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


def edit_name(request):
    new_name = request.POST.get('name')
    try:
        this_user = User.objects.get(id=request.user.id)
        this_user.username = new_name
        this_user.save()
        return HttpResponse(True)
    except:
        return HttpResponse(False)  


def edit_pass(request):
    try:
        new_password = request.POST.get('password')
        this_user = User.objects.get(id=request.user.id)
        this_user.set_password(new_password)
        this_user.save()
        return HttpResponse(True)
    except:
        return HttpResponse(False)


def edit_all(request):
    try:
        new_name = request.POST.get('name')
        new_password = request.POST.get('password')
        this_user = User.objects.get(id=request.user.id)
        this_user.username = new_name
        this_user.save()
        this_user.set_password(new_password)
        this_user.save()
        return HttpResponse(True)
    except:
        return HttpResponse(False)