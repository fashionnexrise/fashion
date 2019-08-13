from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from myblog.models import Post


# Create your views here.
def home(request):
    return render(request, 'myblog/index.html')


def mens(request):
    posts = {'name': Post.objects.all()}
#    return HttpResponse(posts)
    return render(request, 'myblog/mens.html', posts)
