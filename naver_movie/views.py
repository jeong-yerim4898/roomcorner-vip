from django.shortcuts import render,get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated ,AllowAny, IsAdminUser
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .permissions import IsAuthorOrReadonly, IsOwnerOnly
from .serializers import CommentSerializer,MovieSerializer,CoronaSerializer
from .models import Comment,Movie,Corona


# Create your views here.
@api_view(['GET'])
def movies(request):
    if request.method == 'GET':
        movies = Movie.objects.all()

        serializer = MovieSerializer(movies,many=True)
        return Response(serializer.data)

@api_view(['GET','POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated|IsAdminUser])
def comment_list_create(request,movie_pk):
    if request.method == 'GET':
        movie = get_object_or_404(Movie, pk=movie_pk)
        comments = movie.comment_set.all()

        serializer = CommentSerializer(comments,many=True)
        return Response(serializer.data)
    else:
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = CommentSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid(raise_exception=True):
            print(request.user)
            serializer.save(user=request.user,movie=movie)
            movie.like_user.add(request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['PUT','DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsOwnerOnly])
def comment_delete_update(request,movie_pk,comment_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    # if not request.user.community.filter(pk=community.pk).exists():
    #     return Response({'detail':'권한이 없습니다.'})

    if request.user==comment.user or request.user.is_superuser:
        if request.method == 'PUT':
            serializer = CommentSerializer(comment,data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        else:
            comment.delete()
            return Response({'id':comment_pk})
    return Response({'detail':'권한이 없습니다.'})

@api_view(['GET'])
def corona_info(request):
    if request.method == 'GET':
        corona_info = Corona.objects.all()

        serializer = CoronaSerializer(corona_info,many=True)
        return Response(serializer.data)