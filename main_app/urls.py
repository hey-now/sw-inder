from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('accounts/signup/', views.signup, name='signup'),
  path('about/', views.about, name='about'),
  path('interests/', views.interests, name='interests'),
  path('detail/', views.profile_detail, name='detail'),
  path('matches/', views.matches, name='matches'),
  path('profiles/create_profile', views.ProfileCreate.as_view(), name='ProfileCreate'),
  path('profile/<int:pk>/update/', views.ProfileUpdate.as_view(), name='profile_update'),
  path('profile/<int:profile_id>/add_photo/', views.add_photo, name='add_photo'),
  path('interests/<int:profile_id>/assoc_interest/<int:interest_id>/', views.assoc_interest, name='assoc_interest'),
  path('interests/<int:profile_id>/remove_interest/<int:interest_id>/', views.remove_interest, name='remove_interest'),
  # path('interests/', views.InterestList.as_view(), name='interests_index'),
  path('interests/<int:pk>/', views.InterestDetail.as_view(), name='interest_detail'),
  path('interests/create/', views.InterestCreate.as_view(), name='interest_create'),
  path('interests/<int:pk>/update/', views.InterestUpdate.as_view(), name='interest_update'),
  path('interests/<int:pk>/delete/', views.InterestDelete.as_view(), name='interest_delete'),
]