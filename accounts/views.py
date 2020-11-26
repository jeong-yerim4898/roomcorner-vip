from django.shortcuts import render,get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated ,AllowAny, IsAdminUser
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import UserSerializer,UserInfoSerializer,GenreSerializer
from .models import User
from django.contrib.auth import get_user_model
from naver_movie.models import Movie,Comment,Genre

from itertools import chain
# Create your views here.

@api_view(['POST'])
def signup(request):
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
    
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = UserSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        #4. 비밀번호 해싱 후 
        user.set_password(request.data.get('password'))
        user.save()

    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def user_info(request,user_name):
    if request.method == 'GET':
        user = get_object_or_404(get_user_model(), username=user_name)

        serializer = UserInfoSerializer(user)
        return Response(serializer.data)

@api_view(['GET'])
def user_recommend(request,user_name):
    genre_query = {'모험':12,'판타지':14,'애니메이션':16,'드라마':18,
    '공포':27,'액션':28,'코미디':35,'역사':36,'서부':37,
    '스릴러':53,'범죄':80,'다큐멘터리':99,
    'SF':878,'미스터리':9648,'음악':10402,'로맨스':10749,
    '가족':10751,'전쟁':10752,'TV영화':10770}
    user =get_object_or_404(get_user_model(),username=user_name)
    like_movies = user.like_movies.all()
    like_genres = {}
    for like_movie in like_movies:
        genres = like_movie.genre.all()
        for genre in genres:
            idx= genre.name
            if idx in like_genres:
                like_genres[genre.name] += 1
            else:
                like_genres[genre.name] = 1
    if like_genres:
        def f(x):
            return x[1]
        like_genres = sorted(like_genres.items(), key=f)
        like_genres = like_genres[-2:]
    querysets=list()
    # for like_genre in like_genres:
    new1 = genre_query[like_genres[0][0]]
    new2 = genre_query[like_genres[1][0]]
    # print(new1,new2)
    # print(Genre.objects.get(pk=new))
        #     querysets.extend(Genre.objects.get(pk=new))
        # result_queryset = list(chain(*querysets))
        # print(result_queryset)
    serializer1 = GenreSerializer(Genre.objects.get(pk=new1))
    queryset = [Genre.objects.get(pk=new1), Genre.objects.get(pk=new2)]
    print(queryset)
    serializer =  GenreSerializer(queryset, many=True)
    return Response(serializer.data)

