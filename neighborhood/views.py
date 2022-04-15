from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Profile,Post,NeighbourHood,Business
import datetime as dt
from django.urls import reverse
from . forms import Registration,UpdateUser,UpdateProfile,PostForm,NeighbourHoodForm,BusinessForm
from django.contrib.auth.models import User
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.core.exceptions import ObjectDoesNotExist
import os
# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    projects = Post.display_posts()
    return render(request, 'home.html',{"posts": projects})
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
def profile(request):
  current_user = request.user
  posts = Post.objects.all()
  user_photos = Post.objects.filter(id = current_user.id).all()
  
  return render(request,'profile/profile.html',{"posts":posts,'user_photos':user_photos,"current_user":current_user})


def users_profile(request,pk):
  user = User.objects.get(pk = pk)
  projects = Post.objects.filter(user = user)
  c_user = request.user
  
  return render(request,'profile/users_profile.html',{"user":user,"projects":projects,"c_user":c_user})
def update_profile(request):
  if request.method == 'POST':
    user_form = UpdateUser(request.POST,instance=request.user)
    profile_form = UpdateProfile(request.POST,request.FILES,instance=request.user.profile)
    if user_form.is_valid() and profile_form.is_valid():
      user_form.save()
      profile_form.save()
      messages.success(request,'Your Profile account has been updated successfully')
      return redirect('profile')
  else:
    user_form = UpdateUser(instance=request.user)
    profile_form = UpdateProfile(instance=request.user.profile) 
  params = {'user_form':user_form,'profile_form':profile_form}
  return render(request,'profile/update.html',params)

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = current_user
            article.save()
        return redirect('home')

    else:
        form = PostForm()
    return render(request, 'new_post.html', {"form": form})
  
def create_hood(request):
    if request.method == 'POST':
        form = NeighbourHoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = request.user.profile
            hood.save()
            return redirect('hood')
    else:
        form = NeighbourHoodForm()
    return render(request, 'newhood.html', {'form': form})
def hoods(request):
    all_hoods = NeighbourHood.objects.all()
    all_hoods = all_hoods[::-1]
    return render(request, 'hoods.html', { 'all_hoods': all_hoods})

def join_hood(request, id):
    neighbourhood = get_object_or_404(NeighbourHood, id=id)
    request.user.profile.neighbourhood = neighbourhood
    request.user.profile.save()
    return redirect('home')


def leave_hood(request, id):
    hood = get_object_or_404(NeighbourHood, id=id)
    request.user.profile.neighbourhood = None
    request.user.profile.save()
    return redirect('home')
  
def single_hood(request, hood_id):
    hood = NeighbourHood.objects.get(id=hood_id)
    business = Business.objects.filter(neighbourhood=hood)
    posts = Post.objects.filter(hood=hood)
    posts = posts[::-1]
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            b_form = form.save(commit=False)
            b_form.neighbourhood = hood
            b_form.user = request.user.profile
            b_form.save()
            return redirect('single-hood', hood.id)
    else:
        form = BusinessForm()
    params = {
        'hood': hood,
        'business': business,
        'form': form,
        'posts': posts
    }
    return render(request, 'single_hood.html', params)
def hood_members(request, hood_id):
    hood = NeighbourHood.objects.get(id=hood_id)
    members = Profile.objects.filter(neighbourhood=hood)
    return render(request, 'members.html', {'members': members})