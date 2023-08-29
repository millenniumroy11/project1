from django.contrib import admin
from django.urls import path
from home import views
from .views import Category_list

urlpatterns = [
   path("",views.index, name='Home'),
   path("about.html",views.about, name='About'),
   path("contact.html",views.contact, name='Contact Us'),
   path("signup.html",views.signup, name='signup'),
   path("login.html",views.user_login, name='login'),
   path("profile.html",views.profile, name='profile'),
   path("logout.html",views.user_logout, name='logout'),
   path("changepass.html",views.changepass, name='changepass'),
   path("categories.html",Category_list.as_view(), name='category_list'),

]