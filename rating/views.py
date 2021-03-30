from django.shortcuts import render
from .models import Ratings
from .serializers import RatingSerializer
from movie.models import Movies
from customer.models import Customer

from rest_framework import generics, viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.views.decorators.csrf import csrf_protect

from customer.models import Customer
from django.utils import timezone

##=============================== GET/POST rating BY customer id====================================
# Create your views here.
# @api_view(['POST'])
# @csrf_protect
# def list_view_rating_by_customer(request):

#     try:
#         user_id = request.data['user_id']

#         ratings = Ratings.objects.filter(user=user_id)
        
#         data    = RatingSerializer(ratings, many=True).data
#         print(len(ratings))
#         return Response(data=data,status=status.HTTP_200_OK)
#     except:
#         return Response({'success':False}, status=status.HTTP_200_OK)
@api_view(['GET'])
def list_view_rating_by_customer(request, user_id):

    try:
        ratings = Ratings.objects.filter(user=user_id)
        data    = RatingSerializer(ratings, many=True).data
        print(len(ratings))
        return Response(data=data,status=status.HTTP_200_OK)
    except:
        return Response({'success':False}, status=status.HTTP_200_OK)

##=============================== GET/POST rating BY movie id====================================
# @api_view(['POST'])
# @csrf_protect
# def list_view_rating_by_movie(request):

#     try:
#         movie_id = request.data['movie_id']
#         ratings  = Ratings.objects.filter(user=movie_id)
#         data     = RatingSerializer(ratings, many=True).data
#         return Response(data=data,status=status.HTTP_200_OK)
#     except:
#         return Response({'success':False}, status=status.HTTP_200_OK)

@api_view(['GET'])
@csrf_protect
def list_view_rating_by_movie(request, movie_id):

    try:
        ratings  = Ratings.objects.filter(movie=movie_id)
        data     = RatingSerializer(ratings, many=True).data
        return Response(data=data,status=status.HTTP_200_OK)
    except:
        return Response({'success':False}, status=status.HTTP_200_OK)


##=============================== POST create rating====================================
def convert_date(time):
    string_time = str(time).split(" ")[0]
    return int(string_time.replace("-", ""))
@api_view(['POST'])
@csrf_protect
def create_rating(request):

    try:
        data        = request.data
        user_id     = data['user_id']
        movie_id    = data['movie_id']
        rating      = data['rating']

        time         = timezone.now()
        time_convert = convert_date(time)
        
        if Ratings.objects.filter(user=user_id) & Ratings.objects.filter(movie=movie_id):
            return Response({"Success": "Rating exsist"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            movie        = Movies.objects.get(movie_id=movie_id)
            customer     = Customer.objects.get(user_id=user_id)
            createRating = Ratings.objects.create(user=customer, movie=movie, rating=rating, time_rating=time_convert)
            data         = RatingSerializer(createRating).data

        return Response(data=data,status=status.HTTP_200_OK)
    except:
        return Response({'success':False}, status=status.HTTP_200_OK)

    # {
    #     "user_id": 9,
    #     "rating": 4.5,
    #     "time_rating": 1073837168,
    #     "movie_id": 14
    # }
