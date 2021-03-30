from django.urls import path
from .views import CustomerViewDetail, RegisterCustomer, LoginCustomer

urlpatterns = [

    path('',CustomerViewDetail.as_view(),name='customer'),
    path('register/',RegisterCustomer.as_view(),name='register'),
    path('login/',LoginCustomer.as_view(),name='login'),

]