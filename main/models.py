from django.db import models
import django.contrib.auth.models


# Create your models here.

class Nation(models.Model):
    nid = models.AutoField(primary_key=True)
    nname = models.CharField(max_length=20, unique=True)


class City(models.Model):
    cid = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=20)
    nation = models.ForeignKey(Nation, on_delete=models.CASCADE)


class Museum(models.Model):
    cid = models.AutoField(primary_key=True)
    mname = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=100, unique=True)
    introduce = models.CharField(max_length=1500)
    img = models.ImageField()
    nation = models.ForeignKey(Nation, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

