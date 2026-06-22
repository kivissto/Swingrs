from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('create-account', views.createAccount, name='create-account'),
    path('forgot-password', views.forgotPassword, name='forgot-password'),
    path('home', views.home, name='home'), 
    path('inbox', views.inbox, name='inbox'),
    path('likes', views.likes, name='likes'),
    path('venues', views.venues, name='venues'),
    path('user', views.user, name='user'),
    path('like/<int:card_id>/', views.likeCard, name='like_card'),
    path('superlike/<int:card_id>/', views.superlikeCard, name='superlike_card'),
    path('messages/<str:user_id>/', views.message_detail, name='message_detail'),
    path('logout', views.logout_view, name='logout'),
    path('edit-profile', views.edit_profile, name='edit_profile'),
    path('settings/', views.settings, name='settings'),
    path('super-likes/', views.super_likes, name='super_likes'),
    path('boosts/', views.boosts, name='boosts'),
    path('premium/', views.premium, name='premium'),
  ]