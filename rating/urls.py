from django.urls import path
from .views import create_rating, list_view_rating_by_movie, list_view_rating_by_customer

urlpatterns = [

    # path('movie',list_view_rating_by_movie,name='movie'),
    path('movie/<int:movie_id>',list_view_rating_by_movie,name='movie'),
    path('customer/<int:user_id>',list_view_rating_by_customer,name='customer'),
    # path('customer',list_view_rating_by_customer,name='customer'),
    path('create/',create_rating,name='create'),

]