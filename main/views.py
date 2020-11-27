from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.views.decorators.clickjacking import xframe_options_exempt

from .models import Museum
from comment.models import Comment
from itertools import chain


def test(request):
    return render(request, 'testing.html')


def index(request):
    return render(request, 'index.html')


# @xframe_options_exempt
def museum(request, pk):
    museumsinfo = Museum.objects.filter(cid=pk)
    mus_comment = Comment.objects.filter(museum=pk)
    context = {"MuseumDetail": museumsinfo, "Comment": mus_comment}
    return render(request, 'museum.html', context)


#


def museums(request):
    return render(request, 'museums.html')
