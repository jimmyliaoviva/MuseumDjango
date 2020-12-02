from django.shortcuts import render
from .models import Nation
from .models import Museum
from comment.models import Comment


def test(request):
    return render(request, 'testing.html')


def index(request):
    # all_country = Nation.objects.all()
    # all_city = City.objects.all()
    var = list()
    return render(request, 'index.html', locals())


# @xframe_options_exempt
def museum(request, pk):
    museumsinfo = Museum.objects.filter(cid=pk)
    mus_comment = Comment.objects.filter(museum=pk)
    context = {"MuseumDetail": museumsinfo, "Comment": mus_comment}
    return render(request, 'museum.html', context)


def museums(request):
    return render(request, 'museums.html')


def add_nation_record(request):
    a_record = Nation(nid=886, nname='台灣')
    a_record.save()



