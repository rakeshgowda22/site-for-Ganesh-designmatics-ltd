from django.shortcuts import render,redirect
from app.models import glxs,login
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.

def home(request):
    if request.method=='POST':
     if request.POST.get("phoneno") and request.POST.get("email"):
      if request.POST.get("password1") and request.POST.get("password2"):
       gl=glxs()
       gl.phoneno=request.POST.get("phoneno")
       gl.email=request.POST.get("email")
       gl.password1=request.POST.get("password1")
       gl.password2=request.POST.get("password2")
       gl.save()
       return redirect(login)
    else:
       return render(request,'santa.html')

def login(request):
   if request.method=='POST':
      phoneno=request.POST['phoneno']
      password=request.POST['password']
      
      User=auth.authenticate(phoneno=phoneno,password=password)
       
      if User is not None:
           auth.login(request,User)
           return render(request,'index.html')
      else:
           messages.info(request,'invalid login')
           return render(request,'index.html')
   else:
      return render(request,'signup.html')