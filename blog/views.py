from django.shortcuts import render
from django.http import HttpResponse
from .models import blogPost

def index(request):
    blog = blogPost.objects.all()
    return render(request,"blog/index.html",{'blog':blog})

def blogpost(request,id):
    blogpost=blogPost.objects.filter(id=id)[0]
    print(blogpost);
    return render(request,"blog/blogpost.html",{'blogpost':blogpost})