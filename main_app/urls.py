from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('accounts/signup/', views.signup, name='signup'),
  path('about/', views.about, name='about'),
  path('interests/', views.interests, name='interests'),
  
  path('profile/view_profile', views.view_profile, name='view_profile'),
  
  path('profile/create_profile', views.create_profile, name='create_profile'),
]