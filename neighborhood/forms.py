from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Post,NeighbourHood,Business
from django.contrib.auth.models import User


# registering user
class Registration(UserCreationForm):
  email = forms.EmailField()

  class Meta:
    model = User
    fields = ['username','email','password1','password2']


    # user post class

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['title','url','description','photo']
    
class NeighbourHoodForm(forms.ModelForm):
    class Meta:
        model = NeighbourHood
        exclude = ('admin',)

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ('user', 'neighbourhood')
class UpdateProfile(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['profile_photo','bio']

class UpdateUser(forms.ModelForm):
  email = forms.EmailField()
  class Meta:
    model = User
    fields = ['username','email']

