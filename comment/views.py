from django.shortcuts import render, get_object_or_404
from .models import Comment
from .serializers import CommentSerializer
from movie.models import Movies
from customer.models import Customer

from rest_framework import generics, viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.views.decorators.csrf import csrf_protect
from django.utils import timezone

# Create your views here.
@api_view(['POST'])
@csrf_protect
def commentlist(request):

    try:
        user_id = request.data['user_id']

        comment = Comment.objects.filter(user=user_id)
        
        data    = CommentSerializer(comment, many=True).data
        print(len(comment))
        return Response(data=data,status=status.HTTP_200_OK)
    except:
        return Response({'success':False}, status=status.HTTP_200_OK)
# {
# "user_id": 20,
# }


@api_view(['POST'])
@csrf_protect
def createcomment(request):

    try:
        print("a")
        data        = request.data
        user_id     = data['user_id']
        movie_id    = data['movie_id']
        content     = data['content']
 
        movies    = Movies.objects.get(movie_id=movie_id)
        customers = Customer.objects.get(user_id=user_id)
        print("2")

        createcomment = Comment.objects.create(user=customers, movie=movies, content=content)
        print("3")
        datajson  = CommentSerializer(createcomment).data

        return Response(data=datajson,status=status.HTTP_200_OK)
    except:
        return Response({'success':False}, status=status.HTTP_400_BAD_REQUEST)

# {
# "user_id": 20,
# "movie_id": 16,
# "content": "This is comment OK"
# }