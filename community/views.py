from django.shortcuts import render,get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated ,AllowAny, IsAdminUser
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .permissions import IsAuthorOrReadonly, IsOwnerOnly
from .serializers import CommunitySerializer,CommunityCommentSerializer
from .models import Community,CommunityComment

# Create your views here.
@api_view(['GET','POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated|IsAdminUser])
def community_list_create(request):
    if request.method == 'GET':
        communities = Community.objects.all() # 데이터 전체 받아오기
        
        serializer = CommunitySerializer(communities,many=True)
        return Response(serializer.data)
    else:
        serializer = CommunitySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)




@api_view(['PUT','DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsOwnerOnly])
def community_update_delete(request,community_pk):
    community = get_object_or_404(Community, pk=community_pk)

    # print(request.user.is_superuser)
    # print(not request.user.community.filter(pk=community.pk).exists())
    # if not request.user.community.filter(pk=community.pk).exists() or request.user.is_superuser:
    #     return Response({'detail':'권한이 없습니다.'})

    if request.user.community.filter(pk=community.pk).exists() or request.user.is_superuser:
        if request.method == 'PUT':
            serializer = CommunitySerializer(community,data= request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        else:
            community.delete()
            return Response({'id':community_pk})
    return Response({'detail':'권한이 없습니다.'})



@api_view(['GET','POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated|IsAdminUser])
def comment_list_create(request,community_pk):
    if request.method == 'GET':
        community = get_object_or_404(Community, pk=community_pk)
        comments = community.communitycomment_set.all()

        serializer = CommunityCommentSerializer(comments,many=True)
        return Response(serializer.data)
    else:
        community = get_object_or_404(Community, pk=community_pk)
        serializer = CommunityCommentSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid(raise_exception=True):
            print(request.user)
            serializer.save(user=request.user,community=community)
            return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['PUT','DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsOwnerOnly])
def comment_delete_update(request,community_pk,communitycomment_pk):
    community = get_object_or_404(Community, pk=community_pk)
    communitycomment = get_object_or_404(CommunityComment, pk=communitycomment_pk)
    
    # print(request.user.communitycomment.filter(pk=))
    if request.user==communitycomment.user or request.user.is_superuser:
        if request.method == 'PUT':
            serializer = CommunityCommentSerializer(communitycomment,data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        else:
            communitycomment.delete()
            return Response({'id':communitycomment_pk})
    return Response({'detail':'권한이 없습니다.'})