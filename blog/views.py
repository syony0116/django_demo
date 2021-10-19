from django.shortcuts import render

# Create your views here.

def blog_home(request):
    return render(request, "blog/index.html")

def blog_post(request):
    return render(request, "blog/index-post.html")

def blog_create(request):
    return render(request, "blog/index-create.html")
