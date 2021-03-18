from django.shortcuts import render, get_object_or_404
from .serializers import CustomerSerializer
from .models import Customer

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
import hashlib
from django.http import JsonResponse
# Create your views here.

class CustomerList(APIView):
    serializer_class = CustomerSerializer

    def post(self, request):
        try:
            id = request.data["user_id"]
            print("1")
            customer = Customer.objects.get(user_id=id)
            print(customer)
            print("2")
            data = CustomerSerializer(customer).data
            return Response(data=data, status=status.HTTP_200_OK)
        except:
            return Response({"success": False}, status=status.HTTP_400_BAD_REQUEST)


class CreateCustomer(APIView):
    serializer_class = CustomerSerializer

    def post(self, request):
        print("1")
        user_name     = request.data['user_name']
        password     = request.data['password']
        name       = request.data['name']
        email       = request.data['email']
        adress       = request.data['adress']
        birthday       = request.data['birthday']
        gender       = request.data['gender']
        print(user_name, password)
        if Customer.objects.filter(user_name=user_name):
            return Response({"Success2": "userName exist"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            print("3")
            passwordend = password.encode('ascii')   
            hash_object = hashlib.md5(passwordend)
            print(hash_object.hexdigest())
            last_id = Customer.objects.all().last().user_id
            createCustomer   = Customer.objects.create(user_id=last_id + 1,
                                                    user_name=user_name,
                                                    password=hash_object.hexdigest(),
                                                    name=name,
                                                    email=email,
                                                    adress= adress,
                                                    birthday=birthday,
                                                    gender=gender
                                                    )
            return Response({"Success3": True}, status=status.HTTP_200_OK)


class SignInCustomer(APIView):
    serializer_class = CustomerSerializer

    def post(self, request):
        try:
            user_name     = request.data['user_name']
            password     = request.data['password']

            passwordend = password.encode('ascii')   
            hash_object = hashlib.md5(passwordend)
            print(hash_object.hexdigest())

            
            if get_object_or_404(Customer, user_name=user_name):
                customer = Customer.objects.get(user_name=user_name)

                if customer.password == hash_object.hexdigest():
                    return Response({"Sign In Success": True}, status=status.HTTP_200_OK)
                else:
                    return Response({"Sign In success:": False}, status=status.HTTP_400_BAD_REQUEST)

        except:
            return Response({"Success1": False}, status=status.HTTP_400_BAD_REQUEST)

