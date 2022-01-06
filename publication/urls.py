from django.urls import path
from .views import PostDetailView, PublicationHomeView, TopicCreateView, TopicUpdateView, TopicDeleteView, TopicListView, \
PostListView, PostCreateView, PostUpdateView, PostDeleteView, PostDetailView, PostSearchView, PostLikeView, PostCommentView


app_name = 'publication'

urlpatterns = [
    path('', PublicationHomeView.as_view(), name='home'),

    path('topic/list/', TopicListView.as_view(), name="list_topic"),
    path('topic/create/', TopicCreateView.as_view(), name='create_topic'),
    path('topic/<slug:slug>/update/', TopicUpdateView.as_view(), name='update_topic'),
    path('topic/<slug:slug>/delete/', TopicDeleteView.as_view(), name='delete_topic'),

    path('post/list/', PostListView.as_view(), name="list_post"),
    path('post/create/', PostCreateView.as_view(), name="create_post"),
    path('post/<slug:slug>/update/', PostUpdateView.as_view(), name='update_post'),
    path('post/<slug:slug>/delete/', PostDeleteView.as_view(), name='delete_post'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name="detail_post"),

    path('post/search', PostSearchView.as_view(), name="search"),
    path('like/', PostLikeView.as_view(), name="like"),
    path('post/<int:pk>/comment/', PostCommentView.as_view(), name="comment"),
]