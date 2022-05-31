from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('basket', views.bucket, name='basket'),
    path('mens', views.mens, name='mens'),
    path('womens', views.womens, name='womens'),
    path('kids', views.kids, name='kids'),
    # path('register', RegisterUser.as_view(), name='register'),
    # path('login', views.login, name='login'),
]
