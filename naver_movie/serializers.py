from rest_framework import serializers
from .models import Movie,Comment

from django.contrib.auth import get_user_model
from naver_movie.models import Movie,Comment,Genre,Corona

User = get_user_model()

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields = ('id','title','rank','audience','poster_url','overview','original_lang','genre','video_id',)


class CoronaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Corona
        fields = '__all__'

        
class CommentSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField("getUsername")

    def getUsername(self, obj):
        return obj.user.username

    class Meta:
        model=Comment
        fields = ('id','content','created_at','rank','updated_at','user_id','username','movie_id',)
