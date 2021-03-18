from django.urls import path
from .views import commentlist, createcomment

urlpatterns = [

    path('',commentlist,name='comment'),
    path('create/',createcomment,name='create'),
   

]