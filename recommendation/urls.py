from django.urls import path
from .views import recommendations

urlpatterns = [

    path('',recommendations,name='recommendations'),

]