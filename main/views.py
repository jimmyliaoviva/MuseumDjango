from django.shortcuts import render
from .models import Nation, City, Museum
from comment.models import Comment
from django.http import HttpResponse, JsonResponse  #新增jsonresponse，協助評論ajax傳值
from django import forms
import django.contrib.auth as auth
from django.contrib.auth.models import User
# Create your views here.
def test(request):
    return render(request, 'testing.html')


def index(request):
    #all_country = Nation.objects.all()
    #all_city = City.objects.all()
    var = list()
    return render(request, 'index.html', locals())


def museums(request):
    return render(request, 'museums.html')


def museum(request):
    return render(request, 'museum.html')

def add_nation_record(request):
   a_record =  Nation(nid=886, nname='台灣')
   a_record.save()
   #a_reocrd = Nation(nid=1)
   #a_reocrd.delete()
   #past_r = Nation(nid=65, nname='新加坡')
   #a_record = City(cid=4, cname='中區', nation=past_r)

   #a_record.save()
#    return HttpResponse('成功')

# def find_country(request):
#     all_country = Nation.objects.all()
#     all_city = City.objects.all()
#     var = list()
#     return render(request, 'index.html', locals())

def get_comment(request):
    from django.conf import settings    #使用print所需
    from django.shortcuts import redirect   #post後重定位
    import json
    from django.http import JsonResponse
    all_comment = Comment.objects.all()
    if request.method == 'POST':  
        #存入此筆comment
        #commentid -> auto
        #commenttime -> auto
        nation = Nation(nid=886)
        city = City(cid=113)
        user = User(id=1)
        museum = Museum(cid=1, nation=nation, city=city)
        comment = request.POST['comment_content']
        TheCommentRecord = Comment(user=user, museum=museum, comment=comment)
        TheCommentRecord.save()

        #ajax回傳最新comment給前端渲染
        all_comment = {}
        org_comment = Comment.objects.all()
        for comment in org_comment:
            all_comment[comment.commentid] = {'user':comment.user.username, 'museum':comment.museum.mname, 'comment':comment.comment, 'commenttime':comment.commenttime}
        return JsonResponse(all_comment, safe=False)
    return render(request, 'museum.html', locals())

def ajax_get_comment(request):
    all_comment = {}
    org_comment = Comment.objects.all()
    for comment in org_comment:
        all_comment[comment.commentid] = {'user':comment.user.username, 'museum':comment.museum.mname, 'comment':comment.comment, 'commenttime':comment.commenttime}
    return JsonResponse(all_comment, safe=False)

def ajax_delete_comment(request):
    print(request.POST['delete_cid'])
    try:
        cid = request.POST['delete_cid']
        delete_comment = Comment.objects.get(commentid=cid)
        delete_comment.delete()
        return HttpResponse('success')
    except:
        return HttpResponse('fail')
    
    
    