from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Profile 

# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'main_app/about.html')

@login_required
def interests(request):
  return render(request, 'main_app/interests.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('/')
    else:
      error_message = 'Invalid signup - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)  

@login_required
def view_profile(request):
  return render(request, 'main_app/profile/view_profile.html')

@login_required
def create_profile(request):
  return render(request, 'main_app/profile/create_profile.html')

class ProfileCreate(CreateView) :
  model = Profile
  fields = ['name', 'species', 'hair_color', 'height', 'home_world', 'about', 'interest', 'img']

