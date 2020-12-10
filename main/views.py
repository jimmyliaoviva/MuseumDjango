from django.shortcuts import render
from .models import Nation, City
from .models import Museum
from comment.models import Comment
from django.http import HttpResponse, JsonResponse  # 新增jsonresponse，協助評論ajax傳值


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


# 博物館搜尋結果頁面
def museums(request):
    return render(request, 'museums.html')


# def add_nation_record(request):
#     a_record = Nation(nid=886, nname='台灣')
#     a_record.save()

# 首頁下拉選單的城市抓取
def ajax_get_city(request):
    nation = request.GET['nation']
    all_city = City.objects.filter(nation=Nation.objects.get(nid=nation))

    # ajax回傳最新comment給前端渲染
    all = {}
    for city in all_city:
        all[city.cid] = {'id': city.cid, 'city': city.cname}
    return JsonResponse(all, safe=False)
