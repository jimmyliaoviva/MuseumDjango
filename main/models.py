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
    mname = models.CharField(max_length=500)
    address = models.CharField(max_length=2000, blank=True)
    introduce = models.CharField(default=None, blank=True, max_length=5000)
    img = models.CharField(default=None, blank=True, max_length=1500)
    longitude = models.FloatField(default=None, blank=True)
    latitude = models.FloatField(default=None, blank=True)
    website = models.URLField(default=None, blank=True, max_length=500)
    nation = models.ForeignKey(Nation, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
