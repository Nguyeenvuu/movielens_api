from django.shortcuts import render
from .models import Comment
from .serializers import CommentSerializer
from movie.models import Movies
from customer.models import Customer

from rest_framework import generics, viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.views.decorators.csrf import csrf_protect


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