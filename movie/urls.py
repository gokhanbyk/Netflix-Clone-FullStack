from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('movie/<int:id>/', movie, name='movie'),
    path('movie/<slug:slug>/', movie_detail, name='movie_detail'),
]
