from django.contrib import admin
from django.urls import path
from .views import StoryListView, StoryDetailView, ChapterDetailView, CreateStoryView, UserProgressView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', StoryListView.as_view(), name='story_list'),
    path('stories/<int:pk>/', StoryDetailView.as_view(), name='story_detail'),
    path('stories/', StoryListView.as_view(), name='story-list'),
    path('chapters/<int:pk>/', ChapterDetailView.as_view(), name='chapter_detail'),
    path('create/', CreateStoryView.as_view(), name='create_story'),
    path('user/<int:pk>/progress/', UserProgressView.as_view(), name='user_progress'),
]
