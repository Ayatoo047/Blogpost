from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('login/', views.loginuser, name = 'login'),
    path('logout/', views.logoutuser, name = 'logout'),
    path('register/', views.Register, name = 'register'),
    path('about/', views.about, name = 'about'),
    path('add/', views.create, name = 'create'),
    path('blogpost/<str:pk>', views.blogpost, name = 'blogpost')
]
