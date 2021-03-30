from django.urls import path
from .views import MovieViewDetail

urlpatterns = [

    path('<int:id>/',MovieViewDetail.as_view(),name='movies'),

]