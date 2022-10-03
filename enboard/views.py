from django.shortcuts import render
from . import models
from .models import Image
from . models import Video
from . models import Text
from django.utils import timezone


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def display(request):
    return render(request, 'display.html')


def screen1(request):

    images = Image.objects.all()
    videos = Video.objects.all()
    texts = Text.objects.all()

    listimag = list(images)
    listvid = list(videos)
    listtext = list(texts)

    listimag = sorted(listimag,key=lambda i: i.time, reverse = True)
    listvid = sorted(listvid, key=lambda i: i.time, reverse=True)
    listtext = sorted(listtext, key=lambda i: i.time, reverse=True)

    present = timezone.now()

    dict = {}
    flag = 0
    mintime = present

    for i in listimag:
        if i.time <= present and i.screenId == 1:
            if i.endtime > present:
                dict = i
                flag = 1
                mintime = i.time
                break

    for i in listvid:
        if mintime <= i.time < present and i.screenId == 1:
            if i.endtime > present:
                dict = i
                flag = 2
                mintime = i.time
                break

    for i in listtext:
        if mintime <= i.time < present and i.screenId == 1:
            if i.endtime > present:
                dict = i
                flag = 3
                mintime = i.time
                break

    if flag == 1:
        return render(request,'screen1.html',{ 'dict' : dict})

    if flag == 2:
        return render(request, 'screen2.html', {'dict': dict})

    else:
        return render(request,'noContent.html')


def screen2(request):

    images = Image.objects.all()
    videos = Video.objects.all()
    texts = Text.objects.all()

    listimag = list(images)
    listvid = list(videos)
    listtext = list(texts)

    listimag = sorted(listimag,key=lambda i: i.time, reverse = True)
    listvid = sorted(listvid, key=lambda i: i.time, reverse=True)
    listtext = sorted(listtext, key=lambda i: i.time, reverse=True)

    present = timezone.now()

    dict = {}
    flag = 0
    mintime = present

    for i in listimag:
        if i.time <= present and i.screenId == 2:
            if i.endtime > present:
                dict = i
                flag = 1
                mintime = i.time
                break

    for i in listvid:
        if mintime <= i.time < present and i.screenId == 2:
            if i.endtime > present:
                dict = i
                flag = 2
                mintime = i.time
                break

    for i in listtext:
        if mintime <= i.time < present and i.screenId == 2:
            if i.endtime > present:
                dict = i
                flag = 3
                mintime = i.time
                break

    if flag == 1:
        return render(request,'screen1.html',{ 'dict' : dict})

    if flag == 2:
        return render(request, 'screen2.html', {'dict': dict})

    else:
        return render(request,'noContent.html')



def screen3(request):

    images = Image.objects.all()
    videos = Video.objects.all()
    texts = Text.objects.all()

    listimag = list(images)
    listvid = list(videos)
    listtext = list(texts)

    listimag = sorted(listimag,key=lambda i: i.time, reverse = True)
    listvid = sorted(listvid, key=lambda i: i.time, reverse=True)
    listtext = sorted(listtext, key=lambda i: i.time, reverse=True)

    present = timezone.now()

    dict = {}
    flag = 0
    mintime = present

    for i in listimag:
        if i.time <= present and i.screenId == 3:
            if i.endtime > present:
                dict = i
                flag = 1
                mintime = i.time
                break

    for i in listvid:
        if mintime <= i.time < present and i.screenId == 3:
            if i.endtime > present:
                dict = i
                flag = 2
                mintime = i.time
                break

    for i in listtext:
        if mintime <= i.time < present and i.screenId == 3:
            if i.endtime > present:
                dict = i
                flag = 3
                mintime = i.time
                break

    if flag == 1:
        return render(request,'screen1.html',{ 'dict' : dict})

    if flag == 2:
        return render(request, 'screen2.html', {'dict': dict})

    else:
        return render(request,'noContent.html')

    
