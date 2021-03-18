from .models import Ratings
from rest_framework import serializers




class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Ratings
        fields  = '__all__'
        

