from . import views
from django.urls import path

urlpatterns = [
    path('',views.login,name='login'),
    path('home',views.home,name='home'),
    path('signup',views.signup,name='signup'),

]