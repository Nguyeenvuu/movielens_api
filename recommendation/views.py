from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

import ast
import datetime
import time

from .models import RecommendedMovies
from movie.models import Movies
# Create your views here.

def convert_movie(movie):
    dict_movie = {}
    dict_movie['movie_id'] = movie.movie_id
    dict_movie['timestamp'] = time.mktime(datetime.datetime.strptime(str(movie.release_date), "%m/%d/%Y").timetuple())
    return dict_movie


@api_view(['POST',])
def recommendations(request):
    data = request.data
    if data:
        userId = data['user_id']
        try:
            recommendations = RecommendedMovies.objects.get(user = userId)

            movies = Movies.objects.all()

            sorted_movies = sorted(movies, key=lambda x: x.popularity, reverse=True)[0:200]
            popularity_movies = [ele.movie_id for ele in sorted_movies]

            print('truoc for')
            movies2 = []
            for movie in movies:
                if (movie.release_date != None):
                    try:
                        temp = int(str(movie.release_date).split('/')[2])
                        if (temp > 2000):
                            dict_movie = convert_movie(movie)
                            movies2.append(dict_movie)
                    except:
                        pass
            print('sau for ok')
            sorted_movies = sorted(movies2, key=lambda x: x['timestamp'], reverse=True)[0:10]
            new_movies = [ele['movie_id'] for ele in sorted_movies]
            print('ok')
            data_json = {
                'success': True,
                'user_id': userId,
                'recommendations': ast.literal_eval(recommendations.recommendations),
                'popularity': popularity_movies,
                'new': new_movies
            }
            print('len recommendations:', len(data_json['recommendations']))
            return Response(data_json, status=status.HTTP_200_OK)
        except:
            return Response({'success1':False}, status=status.HTTP_200_OK)
    else:
        return Response({'success2':False}, status=status.HTTP_200_OK)