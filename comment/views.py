from django.shortcuts import render
# Create your views here.
from main.models import Nation, City, Museum
from comment.models import Comment
from django.http import HttpResponse, JsonResponse  # 新增jsonresponse，協助評論ajax傳值

from django.contrib.auth.models import User


# def Add_comment(request):
#     post_comment = request.POST.Get('SendComment','')
#     user_comment = Comment( comment=post_comment)


def ajax_add_comment(request):
    from django.http import JsonResponse
    nation = Nation(nid=886)
    city = City(cid=113)
    user = User(id=1)
    museum = Museum(cid=1, nation=nation, city=city)
    comment = request.POST['comment_content']
    theCommentRecord = Comment(user=user, museum=museum, comment=comment)
    theCommentRecord.save()

    # ajax回傳最新comment給前端渲染
    all_comment = {}
    org_comment = Comment.objects.all()
    for comment in org_comment:
        all_comment[comment.commentid] = {'user': comment.user.username, 'museum': comment.museum.mname,
                                          'comment': comment.comment, 'commenttime': comment.commenttime}
    return JsonResponse(all_comment, safe=False)


def ajax_get_comment(request):
    all_comment = {}
    org_comment = Comment.objects.all()
    for comment in org_comment:
        all_comment[comment.commentid] = {'user': comment.user.username, 'museum': comment.museum.mname,
                                          'comment': comment.comment, 'commenttime': comment.commenttime}
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
