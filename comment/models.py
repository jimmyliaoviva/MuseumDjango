from django.db import models
import django.contrib.auth.models
import main.models
# Create your models here.

class Comment(models.Model) :
    commentid = models.AutoField(primary_key=True)
    user = models.ForeignKey(django.contrib.auth.models.User,on_delete=models.CASCADE)
    museum = models.ForeignKey(main.models.Museum,on_delete=models.CASCADE)
    comment = models.CharField(max_length=1500)
    commenttime = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('commenttime',)