from django.urls import path

from .views import PostViewSet, PostList

urlpatterns = [
    path('post/', PostViewSet.as_view({'get': 'list'}), name='post'),
    path('post/<int:post_pk>/', PostViewSet.as_view({'get': 'retrieve'}), name='post-detail'),
    path('posts-list/', PostList.as_view(), name='posts-list'),
]
