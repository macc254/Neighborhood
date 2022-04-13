from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Profile,Post
from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from django.urls import reverse
from . forms import Registration,UpdateUser,UpdateProfile,PostForm
from django.contrib.auth.models import User
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.core.exceptions import ObjectDoesNotExist
import os
# Create your views here.
def home(request):
    return render(request, 'home.html')
def register(request):
  if request.method == 'POST':
    form = Registration(request.POST)
    if form.is_valid():
      form.save()
      email = form.cleaned_data['email']
      username = form.cleaned_data.get('username')

      messages.success(request,f'Account for {username} created,you can now login')
      return redirect('registration/login.html')
  else:
    form = Registration()
  return render(request,'registration/registration_form.html',{"form":form})


@login_required(login_url='/accounts/login/')
def post(request):
  if request.method == 'POST':
    post_form = PostForm(request.POST,request.FILES) 
    if post_form.is_valid():
      the_post = post_form.save(commit = False)
      the_post.user = request.user
      the_post.save()
      return redirect('home')

  else:
    post_form = PostForm()
  return render(request,'post.html',{"post_form":post_form})