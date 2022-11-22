from django.db import models
import random 
from django.urls import reverse 

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

  def get_absolute_url(self):
    return reverse('view_profile', kwargs={'pk': self.id})