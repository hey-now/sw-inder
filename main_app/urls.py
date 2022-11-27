from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('accounts/signup/', views.signup, name='signup'),
  path('about/', views.about, name='about'),
  path('interests/', views.interests, name='interests'),
  path('profiles/<int:profile_id>/add_photo/', views.add_photo, name='add_photo'),
  path('profiles/', views.profile_detail.as_view(), name='detail'),
  path('profiles/create_profile', views.ProfileCreate.as_view(), name='ProfileCreate'),
]