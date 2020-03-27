from django.shortcuts import render,HttpResponse
from .models import Post
# Create your views here.
def blogHome(request):
    allpost=Post.objects.all()
    context={'allpost':allpost}
    print(allpost)
    return render(request,'blog/blogHome.html',context)

def blogPost(request,slug):
    post=Post.objects.filter(slug=slug)[0]
    context={'post':post}
    return render(request,'blog/blogPost.html',context)