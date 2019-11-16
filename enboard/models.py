from django.shortcuts import render
from django.db import models


class Image(models.Model):
    image = models.ImageField(upload_to='images/', default='NULL')
    time = models.DateTimeField()
    endtime = models.DateTimeField()
    user = models.CharField(max_length=500)
    screenId = models.BigIntegerField()


class Video(models.Model):
    user = models.CharField(max_length=50)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")
    time = models.DateTimeField()
    endtime = models.DateTimeField()
    screenId = models.BigIntegerField()


class Text(models.Model):
    text = models.CharField(max_length=1000)
    time = models.DateTimeField()
    endtime = models.DateTimeField()
    screenId = models.BigIntegerField()
    user = models.CharField(max_length=50)
