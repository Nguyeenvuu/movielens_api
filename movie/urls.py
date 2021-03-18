from django.urls import path
from .views import MovieList

urlpatterns = [

    path('<int:id>/',MovieList.as_view(),name='movies'),

]