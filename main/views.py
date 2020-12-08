from django.shortcuts import render
from .models import Nation, City
from .models import Museum
from comment.models import Comment
from django.http import HttpResponse, JsonResponse  # 新增jsonresponse，協助評論ajax傳值


def test(request):
    return render(request, 'testing.html')


def index(request):
    all_country = Nation.objects.all()
    # all_city = City.objects.all()
    var = list()
    return render(request, 'index.html', locals())


# @xframe_options_exempt
def museum(request, pk):
    museumsinfo = Museum.objects.filter(cid=pk)
    mus_comment = Comment.objects.filter(museum=pk)
    context = {"MuseumDetail": museumsinfo, "Comment": mus_comment}
    return render(request, 'museum.html', context)

#search
def museums(request):
    museumsearchnation = request.POST.get('countrySearch', '')
    museumsearchcity = request.POST.get('citySearch', '')
    museumsearch = request.POST.get('museumSearch', '')
    if museumsearchnation != '':
        if museumsearchcity != '':
            if museumsearch != '':
                museumsearchresult = Museum.objects.filter(city=museumsearchcity,mname__icontains=museumsearch)
            else :
                museumsearchresult = Museum.objects.filter(city=museumsearchcity)
        else:
            if museumsearch != '':
                museumsearchresult = Museum.objects.filter(nation=museumsearchnation,mname__icontains=museumsearch)
            else:
                museumsearchresult = Museum.objects.filter(nation=museumsearchnation)
    else:
        museumsearchresult = Museum.objects.filter(mname__icontains=museumsearch)
    context = {"SearchResult": museumsearchresult}
    return render(request, 'museums.html', context)


def add_nation_record(request):
    a_record = Nation(nid=886, nname='台灣')
    a_record.save()


def ajax_get_city(request):
    nation = request.GET['nation']
    all_city = City.objects.filter(nation=Nation.objects.get(nid=nation))

    # ajax回傳最新comment給前端渲染
    all = {}
    for city in all_city:
        all[city.cid] = {'id': city.cid, 'city': city.cname}
    return JsonResponse(all, safe=False)
