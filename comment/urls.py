from django.urls import path
from .views import commentlist

urlpatterns = [

    path('',commentlist,name='comment'),
   

]