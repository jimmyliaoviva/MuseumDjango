from django.shortcuts import render
from .models import Nation, City
from .models import Museum
from comment.models import Comment
from django.http import HttpResponse, JsonResponse  # 新增jsonresponse，協助評論ajax傳值
from django.core.paginator import Paginator


# 測試用
def test(request):
    return render(request, 'testing.html')


# 首頁
def index(request):
    all_country = Nation.objects.all()
    # all_city = City.objects.all()
    var = list()
    return render(request, 'index.html', locals())


def about(request):
    return render(request, 'about.html')


# 每個博物館的頁面
# @xframe_options_exempt
def museum(request, pk):
    museumsinfo = Museum.objects.filter(cid=pk)
    mus_comment = Comment.objects.filter(museum=pk)
    context = {"MuseumDetail": museumsinfo, "Comment": mus_comment, "pk": pk}
    return render(request, 'museum.html', context)


def museums(request):
    museumsearchnation = request.GET.get('countrySearch', '')
    museumsearchcity = request.GET.get('citySearch', '')
    museumsearch = request.GET.get('museumSearch', '')
    page_number = request.GET.get('page')
    if museumsearchnation != '':
        if museumsearchcity != '':
            if museumsearch != '':
                museumsearchresult = Museum.objects.filter(city=museumsearchcity, mname__icontains=museumsearch)
            else:
                museumsearchresult = Museum.objects.filter(city=museumsearchcity)
        else:
            if museumsearch != '':
                museumsearchresult = Museum.objects.filter(nation=museumsearchnation, mname__icontains=museumsearch)
            else:
                museumsearchresult = Museum.objects.filter(nation=museumsearchnation)
    else:
        museumsearchresult = Museum.objects.filter(mname__icontains=museumsearch)
    paginator = Paginator(museumsearchresult, 25)
    searchResult = museumsearchresult
    page_obj = paginator.get_page(page_number)
    # context = {"SearchResult": museumsearchresult}
    url = "museums?countrySearch=" + museumsearchnation + "&citySearch=" + museumsearchcity + "&museumSearch=" + museumsearch
    result = {'page_obj': page_obj, 'searchResult': searchResult, 'url': url}
    return render(request, 'museums.html', result)


# 首頁下拉選單的城市抓取
def ajax_get_city(request):
    nation = request.GET['nation']
    all_city = City.objects.filter(nation=Nation.objects.get(nid=nation))

    # ajax回傳最新comment給前端渲染
    all = {}
    for city in all_city:
        all[city.cid] = {'id': city.cid, 'city': city.cname}
    return JsonResponse(all, safe=False)


from django.core import serializers


def download(request):
    all_nation = list(Nation.objects.all().only())
    all_city = list(City.objects.all().only())
    all_museum = list(Museum.objects.all().only())
    all_comment = list(Comment.objects.all().only())
    all_list_data = all_nation + all_city + all_museum + all_comment
    all_data = serializers.serialize('json', all_list_data)
    response = HttpResponse(content=all_data)
    response['Content-Type'] = 'text/json'
    response['Content-Disposition'] = 'attachment; filename="data.json"'
    return response
