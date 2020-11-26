from rest_framework import serializers
from django.contrib.auth import get_user_model
from naver_movie.models import Movie,Comment,Genre

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields = ('username','password',)

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ('username','is_staff',)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model=Genre
        fields = '__all__'
