from rest_framework import viewsets, status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    def get(self, request, post_pk):
        try:
            post = Post.objects.get(pk=post_pk, user=request.user)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostList(ListAPIView):

    def get(self, request):
        posts = Post.objects.filter(is_active=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)