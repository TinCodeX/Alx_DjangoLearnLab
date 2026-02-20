from rest_framework import serializers
from .models import Post, Comment, Like
from accounts.serializers import UserProfileSerializer

class CommentSerializer(serializers.ModelSerializer):
    author = UserProfileSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at']


class PostSerializer(serializers.ModelSerializer):
    author = UserProfileSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)  
    likes_count = serializers.IntegerField(source='likes.count', read_only=True)# nested comments

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at', 'comments', 'likes_count']