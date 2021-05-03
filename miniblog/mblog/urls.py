# from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    
    path('', views.home, name='homeName'),
    path('about/', views.about, name='aboutName'),
    path('contact/', views.contact, name='contactName'),
    path('dashboard/', views.dashboard, name='dashboardName'),
    path('signup/', views.user_signup, name='signupName'),
    path('login/', views.user_login, name='loginName'),
    path('logout/', views.user_logout, name='logoutName'),
    path('addpost/', views.add_post, name='addpostName'),
    path('updatepost/<int:id>', views.update_post, name='updatepostName'),
    path('delete/<int:id>', views.delete_post, name='deletepostName'),
   
]
