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
from .models import Profile, Photo, Interest

baseUrl = 'https://swapi.dev/api/'
r = requests.get(baseUrl + 'people/1')
r2 = requests.get('http://swapi.dev/api/planets/1')
people = r.json()




img = [
  'https://imgur.com/b4GrpJb.png', # luke and numb 1
  'https://imgur.com/IFG02gN.pnng', # c-3po 2
  'https://imgur.com/5ebf0mo.png', # r2-d2 3
  'https://imgur.com/1HICt2k.jpeg',  # darth vader and num 4
  'https://imgur.com/HQjQeIx.png', #leia 5
  'https://imgur.com/kh6Oqlo.png',  #owen lars 6
  'https://imgur.com/HzTNVj1.png',  # beru 7
  'https://imgur.com/EUAFFcA.png', # r5-d4 8
  'https://imgur.com/aoqXU2e.png',  #  biggs 9
  'https://imgur.com/zfYrKRx.png',  # obi wan 10
  'https://imgur.com/57ngyTT.png',  # anakin 11
  'https://imgur.com/oRj5kom.png',  # wwillhuff 12
  'https://imgur.com/7GlhiV6.png', # chewy 13
  'https://imgur.com/ZeuboXl.png',  # han solo 14
  'https://imgur.com/QMu4ni1.png', # greedo 15
  'https://imgur.com/VBxeNwT.png',  # jabba 16
  'https://imgur.com/Z5s6APX.png',   # gorilla with sunglasses 17
  'https://imgur.com/UQvY2ec.png',  # wedge antilles 18
  'https://imgur.com/Lcwknoz.png', # jek tono porkins 19
  'https://imgur.com/lzHfii9.png', #  yoda 20
  'https://imgur.com/4W39iIq.png', # palpy 21
  'https://imgur.com/h7PrcY2.png',  #  boba 22
  'https://imgur.com/84eB0oN.png', # ig-88 23
  'https://imgur.com/1bKIIv8.png',  # bossk 24
  'https://imgur.com/OXaYGXX.png', #  lando 25
  'https://imgur.com/WG4qXwI.png',  # lobot 26
  'https://imgur.com/rsLgCOM.png', # ackbar 27
  'https://imgur.com/R3F3LnB.png', # mon mothma 28
  'https://imgur.com/RQ6yHFg.png',  # arvel crynyd 29
  'https://imgur.com/jDhVXQy.png',  #  wicket 30
  'https://imgur.com/6qamhZu.png', # nien numb 31
  'https://imgur.com/j5JaqM1.png', # qui gon 32
  'https://imgur.com/JJF7FRf.png', # nute gunray 33
  'https://imgur.com/w732wXd.png', # finis valorum 34
  'https://imgur.com/lI7gdQg.png', # padme 35
  'https://imgur.com/8Q4W7jG.png', # jar jar 36
  'https://imgur.com/rmI8rgU.png', # roos tarpals 37
  'https://imgur.com/yXDhoUQ.png', # rugor nass 38
  'https://imgur.com/LpwGYws.png', # ric olie 39
  'https://imgur.com/EIMot31.png', # watto 40
  'https://imgur.com/tSoIPDF.png', # sebulba 41
  'https://imgur.com/hWfV41y.png', # quarsh panaka 42
  'https://imgur.com/kBNvrrK.png', # shmi 43
  'https://imgur.com/NF3CTDm.png', # darth maul 44
  'https://imgur.com/lmd9feE.png', # bib fortuna 45
  'https://imgur.com/IDSVFMZ.png', # ayla secura 46
  'https://imgur.com/nVw9ijO.png', # ratts tyerel 47
  'https://imgur.com/kfIP4li.png', # dud bolt 48
  'https://imgur.com/w6blxA0.png', # gasgano 49
  'https://imgur.com/KTBo3pf.png', # ben quadinaros 50
  'https://imgur.com/HPTJokQ.png', # mace windu 51
  'https://imgur.com/hVYXuwT.png', # ki-adi-mundi 52
  'https://imgur.com/Ncjhgsr.png', # kit fisto 53
  'https://imgur.com/3IEiIvZ.png', # eeth koth 54
  'https://imgur.com/KAFQrwW.png', # adi gallia 55
  'https://imgur.com/rL8RDlu.png', # saesee tiin 56
  'https://imgur.com/3ErWWx1.png', # yarael poof 57
]



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

class ProfileUpdate(UpdateView):
  model = Profile
  fields = ['name', 'species', 'hair_color', 'height', 'homeworld', 'about']

@login_required
def profile_detail(request):
  profile = Profile.objects.get(user=request.user)
  return render(request, 'main_app/detail.html', { 
    'profile': profile,
    'interests': interests
  })

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'main_app/about.html')

@login_required
def interests(request):
  return render(request, 'main_app/interests.html')

class InterestList(ListView):
  model = Interest

class InterestDetail(DetailView):
  model = Interest

class InterestCreate(CreateView):
  model = Interest
  fields = '__all__'

class InterestUpdate(UpdateView):
  model = Interest
  fields = ['__all__']

class InterestDelete(DeleteView):
  model = Interest
  success_url = '/interests'

def assoc_interest(request, profile_id, interest_id):
  Profile.objects.get(id=profile_id).interests.add(interest_id)
  return redirect('detail', profile_id=profile_id)

def remove_interest(request, profile_id, interest_id):
  Profile.objects.get(id=profile_id).interests.remove(interest_id)
  return redirect('detail', profile_id=profile_id)

@login_required
def matches(request):
  rand_num = random.randint(1, 82)
  baseUrl = 'https://swapi.dev/api/'
  r = requests.get(baseUrl + 'people/' + str(rand_num))
  people = r.json()
  name = people['name']
  species = people['species']
  img_gen = []
  try: 
    img_gen = img[rand_num - 1]
  except IndexError:
    pass
  if not species:
    species_name = 'Unidentified Life-Form'
  else:
    species_req = requests.get(species[0])
    species_data = species_req.json()
    species_name = species_data['name']
  hair_color = people['hair_color'].capitalize()
  gender = people['gender'].capitalize()
  homeworld = people['homeworld']
  homeworld_req = requests.get(homeworld)
  homeworld_data = homeworld_req.json()
  homeworld_name = homeworld_data['name']
  return render(request, 'main_app/matches.html', { 'name': name, 'hair_color': hair_color, 'gender': gender, 'homeworld_name': homeworld_name, 'species_name': species_name, 'img_gen': img_gen})

def add_photo(request, profile_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      bucket = os.environ['S3_BUCKET']
      s3.upload_fileobj(photo_file, bucket, key)
      url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
      Photo.objects.create(url=url, profile_id=profile_id)
    except Exception as e:
      print('An error occured uploading file to S3')
      print(e)
  return redirect('detail')






# @login_required
# def profile_detail(request):
#   profile = Profile.objects.filter(user=request.user)
#   return render(request, 'profiles/detail.html', {'profile': profile})

# @login_required
# class CreateProfile(loginRequiredMixin, CreateView):
#   model = Profile
#   fields = ['name', 'species', 'hair_color', 'height', 'homeworld', 'about', ]
#   # return render(request, 'main_app/profile/create_profile.html')