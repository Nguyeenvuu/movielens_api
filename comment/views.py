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
def list_comment_by_customer(request):

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
def list_comment_by_movie(request):

    try:
        movie_id = request.data['movie_id']
        comment  = Comment.objects.filter(movie=movie_id)
        data     = CommentSerializer(comment, many=True).data
        return Response(data=data,status=status.HTTP_200_OK)
    except:
        return Response({'success':False}, status=status.HTTP_200_OK)


@api_view(['POST'])
@csrf_protect
def create_comment(request):

    try:
        data        = request.data
        user_id     = data['user_id']
        movie_id    = data['movie_id']
        content     = data['content']
 
        movies    = Movies.objects.get(movie_id=movie_id)
        customers = Customer.objects.get(user_id=user_id)

        createcomment = Comment.objects.create(user=customers, movie=movies, content=content)
        datajson      = CommentSerializer(createcomment).data

        return Response(data=datajson,status=status.HTTP_200_OK)
    except:
        return Response({'success':False}, status=status.HTTP_400_BAD_REQUEST)

# {
# "user_id": 20,
# "movie_id": 16,
# "content": "This is comment OK"
# }