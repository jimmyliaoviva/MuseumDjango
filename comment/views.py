from django.shortcuts import render
from comment.models import Comment
# Create your views here.
from django.views import generic
from .models import Comment
import datetime




def Add_comment(request):
    post_comment = request.POST.Get('SendComment','')
    user_comment = Comment( comment=post_comment)


