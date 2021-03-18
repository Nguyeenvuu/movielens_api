from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Movies
from .serializers import MovieSerializer

# Create your views here.

class MovieList(APIView):
    def get(self, request, id):
        movies = Movies.objects.get(movie_id=id)
        data   = MovieSerializer(movies).data
        return Response(data=data) 
