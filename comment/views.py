from django.shortcuts import render
# Create your views here.
from main.models import Nation, City, Museum
from comment.models import Comment
from django.http import HttpResponse, JsonResponse  # 新增jsonresponse，協助評論ajax傳值
from django.contrib.auth.models import User


def ajax_get_comment(request):
    museumId = request.POST['museumId']
    all_comment = {}
    org_comment = Comment.objects.filter(museum_id=museumId)
    for comment in org_comment:
        all_comment[comment.commentid] = {'user': comment.user.username, 'userId': comment.user_id,
                                          'museum': comment.museum.mname,
                                          'comment': comment.comment,
                                          'commentTime': comment.commenttime.strftime("%Y.%m.%d")}
    return JsonResponse(all_comment, safe=False)


def ajax_add_comment(request):
    user = User(id=request.user.id)
    comment = request.POST['comment_content']
    museumId = request.POST['museumId']
    museum = Museum(cid=museumId)
    theCommentRecord = Comment(user=user, museum=museum, comment=comment)
    theCommentRecord.save()

    return ajax_get_comment(request)


def ajax_delete_comment(request):
    try:
        cid = request.POST['delete_cid']
        delete_comment = Comment.objects.get(commentid=cid)
        delete_comment.delete()
        return HttpResponse('success')
    except:
        return HttpResponse('fail')


def ajax_save_comment(request):
    commentId = request.POST['commentId']
    comment = request.POST['comment_content']
    commentToUpdate = Comment.objects.get(commentid=commentId)
    commentToUpdate.comment = comment
    commentToUpdate.save()

    return ajax_get_comment(request)
