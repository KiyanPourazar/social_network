from django.urls import path

from .views import PostViewSet, PostList, CommentView, LikeView

urlpatterns = [
    path('post/', PostViewSet.as_view({'get': 'list'}), name='post'),
    path('post/<int:post_pk>/', PostViewSet.as_view({'get': 'retrieve'}), name='post-detail'),
    path('posts-list/', PostList.as_view(), name='posts-list'),
    path('post/<int:post_pk>/comments/', CommentView.as_view(), name='comment'),
    path('post/<int:post_pk>/likes/', LikeView.as_view(), name='like'),
]
