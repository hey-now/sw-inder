import os
import uuid
import boto3
import requests
import random
from pprint import pprint
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Profile, Photo

baseUrl = 'https://swapi.dev/api/'
r = requests.get(baseUrl + 'people/1')
r2 = requests.get('http://swapi.dev/api/planets/1')
people = r.json()



# Create your views here.
def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('/profiles/create_profile')
    else:
      error_message = 'Invalid signup - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)  

class ProfileCreate(LoginRequiredMixin, CreateView) :
  model = Profile
  fields = ['name', 'species', 'hair_color', 'height', 'homeworld', 'about']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

@login_required
def profile_detail(request):
  profile = Profile.objects.all() 
  return render(request, 'main_app/detail.html', { 'profile': profile })

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'main_app/about.html')

@login_required
def interests(request):
  return render(request, 'main_app/interests.html')

@login_required
def matches(request):
  rand_num = random.randint(1, 82)
  baseUrl = 'https://swapi.dev/api/'
  r = requests.get(baseUrl + 'people/' + str(rand_num))
  people = r.json()
  name = people['name']
  return render(request, 'main_app/matches.html', { 'name': name })

def add_photo(request):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      bucket = os.environ['S3_BUCKET']
      s3.upload_fileobj(photo_file, bucket, key)
      url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
      Photo.objects.create(url=url)
    except Exception as e:
      print('An error occured uploading file to S3')
      print(e)
  return redirect('profile_form.html')




# @login_required
# def profile_detail(request):
#   profile = Profile.objects.filter(user=request.user)
#   return render(request, 'profiles/detail.html', {'profile': profile})

# @login_required
# class CreateProfile(loginRequiredMixin, CreateView):
#   model = Profile
#   fields = ['name', 'species', 'hair_color', 'height', 'homeworld', 'about', ]
#   # return render(request, 'main_app/profile/create_profile.html')