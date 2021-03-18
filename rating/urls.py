from django.urls import path
from .views import ratingListView, ratingCreate

urlpatterns = [

    path('',ratingListView,name='ratings'),
    path('create/',ratingCreate,name='create'),

]