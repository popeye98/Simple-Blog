from django.shortcuts import render
from .models import Author
from blog.models import Post
# Create your views here.
def AboutAuthor(request,slug):
    author=Author.objects.filter(Slug=slug)[0]
    print(author)
    param={'author':author}
    print(author)
    return render(request,'author/about.html',param)

def AllAuthor(request):
    author=Author.objects.all()
    print(author)
    param={'author':author}
    return render(request,'author/all.html',param)






