from .models import RecommendedMovies
from rest_framework import serializers

class RecommendationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model   = RecommendedMovies
        fields  =['user', 'recommendations']