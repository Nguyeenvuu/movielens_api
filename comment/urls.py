from django.urls import path
from .views import list_comment_by_customer,list_comment_by_movie, create_comment

urlpatterns = [

    path('customer',list_comment_by_customer,name='customer'),
    path('movie',list_comment_by_movie,name='movie'),
    path('create/',create_comment,name='create'),
   

]