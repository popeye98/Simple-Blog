from django.shortcuts import render,HttpResponse,redirect
from home.models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from blog.models import Post
# Create your views here.
def home(request):
    return render(request,'home/home.html')

def contact(request):

    if request.method=='POST':
        #print ('we are using post request')
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        content=request.POST['content']        

        if(len(name)<4 or len(email)<5 or len(phone)<10 or len(content)<4):
            messages.error(request, 'Please fill the form correctly')
        else:
            contact=Contact(name=name,phone=phone,email=email,content=content)
            contact.save()
            messages.success(request,'Your request has been successfully recorded')
    return render(request,'home/contact.html')
    
def about(request):
    return render(request,'home/about.html')

def search(request):
    query=request.GET['query']
    if len(query)>78:
        allposts=Post.objects.none()
    else:
        allpostsTitle=Post.objects.filter(title__icontains=query )
        allpostsContent=Post.objects.filter(content__icontains=query )
        allpostsAuthor=Post.objects.filter(author__icontains=query )
        allposts=allpostsAuthor.union(allpostsContent,allpostsTitle)

    if allposts.count()==0:
        messages.warning(request, 'No search result found please refine your query')
        

    param={'allpost':allposts ,'query':query}
    return render(request,'home/search.html',param)

def handlesignup(request):
    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        #validation

        if len(username)>10:
            messages.error(request,"Must be less than 10 character")
            return redirect(home)
        
        if not username.isalnum():
            messages.error(request,"Username must be of alpha numneric")
            return redirect(home)
        
        if pass1!=pass2:
            messages.error(request,"Both password should be matched")
            return redirect(home)





        newuser=User.objects.create_user(username,email,pass1)
        newuser.first_name=fname        
        newuser.last_name=lname     
        newuser.save()
        messages.success(request,"Succesfuly created your new account")
        return redirect('home')


    else:
        return render(request,'home/error404.html')

def handlelogin(request):
    if request.method=='POST':
        username=request.POST['loginusername']
        login_password=request.POST['pass']
        user=authenticate(username=username,password=login_password)
        if user is not None:
            login(request,user)
            messages.success(request,f"Successfully login as {username}")
            return redirect('home')
        else:
            messages.error(request,"please try again")
            return redirect ('home')
    

def handlelogout(request):
    logout(request)
    messages.success(request,"succsssfullt logout")
    return redirect('home')