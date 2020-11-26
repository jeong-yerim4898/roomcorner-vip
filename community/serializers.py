from rest_framework import serializers
from .models import Community , CommunityComment

class CommunitySerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField("getUsername")

    def getUsername(self, obj):
        return obj.user.username

    class Meta:
        model=Community
        fields = ('id','title','content','created_at','updated_at','username')



class CommunityCommentSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField("getUsername")

    def getUsername(self, obj):
        return obj.user.username

    class Meta:
        model=CommunityComment
        fields = ('id','content','created_at','updated_at','user_id','username','community_id')
