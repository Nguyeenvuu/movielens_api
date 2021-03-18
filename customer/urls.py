from django.urls import path
from .views import CustomerList, CreateCustomer, SignInCustomer

urlpatterns = [

    path('',CustomerList.as_view(),name='movies'),
    path('create/',CreateCustomer.as_view(),name='create'),
    path('signin/',SignInCustomer.as_view(),name='signin'),


]