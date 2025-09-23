from django.contrib.auth import get_user_model

from rest_framework import serializers

from posts.models import Post

User = get_user_model()

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id' ,'user', 'title', 'caption', 'is_active', 'is_public')
        extra = {
            'user': {"read_only" : True},
        }
