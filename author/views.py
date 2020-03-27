from django.shortcuts import render
from .models import Author
# Create your views here.
def AboutAuthor(request,slug):
    author=Author.objects.filter(slug=slug)
    param={author:author}
    render(request,'author/about.html',param)
