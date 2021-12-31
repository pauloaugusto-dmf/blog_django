from django.urls import path
from .views import PublicationHomeView, TopicCreateView, TopicUpdateView, TopicDeleteView, TopicListView


app_name = 'publication'

urlpatterns = [
    path('', PublicationHomeView.as_view(), name='home'),
    path('topic/list/', TopicListView.as_view(), name="list_topic"),
    path('topic/create/', TopicCreateView.as_view(), name='create_topic'),
    path('topic/<slug:slug>/update/', TopicUpdateView.as_view(), name='update_topic'),
    path('topic/<slug:slug>/delete/', TopicDeleteView.as_view(), name='delete_topic'),
]