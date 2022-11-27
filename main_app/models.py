from django.db import models
import random 
from django.urls import reverse 
from django.contrib.auth.models import User

# Create your models here.


def get_match():
  match = random.random(82)
  print(match)

class Profile(models.Model):
  name = models.CharField(max_length=50)
  species = models.CharField(max_length=50)
  hair_color = models.CharField(max_length=50)
  height = models.CharField(max_length=50)
  homeworld = models.CharField(max_length=50)
  about = models.CharField(max_length=50)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def get_absolute_url(self):
    return reverse('detail', kwargs={'profile_id': self.id})

class Photo(models.Model):
    url = models.CharField(max_length=200)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    # def __str__(self):
    #     return f"Photo for cat_id: {self.cat_id} @{self.url}"
