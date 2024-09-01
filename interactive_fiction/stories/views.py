from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Story, Chapter, Choice, UserProgress
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import StorySerializer # , ChapterSerializer, ChoiceSerializer, UserProgressSerializer

# API View for listing all stories
class StoryListView(APIView):
    def get(self, request):
        stories = Story.objects.all()
        serializer = StorySerializer(stories, many=True)
        return Response(serializer.data)

# API View for getting the details of a specific story
class StoryDetailView(APIView):
    def get(self, request, pk):
        story = get_object_or_404(Story, pk=pk)
        serializer = StorySerializer(story)
        return Response(serializer.data)

# API View for getting the details of a specific chapter
# class ChapterDetailView(APIView):
#     @method_decorator(login_required)
#     def post(self, request, pk):
#         chapter = get_object_or_404(Chapter, pk=pk)
#         choice_id = request.data.get('choice_id')
#         choice = get_object_or_404(Choice, id=choice_id)

#         # Update user progress
#         progress, created = UserProgress.objects.get_or_create(
#             user=request.user,
#             story=chapter.story,
#             defaults={'current_chapter': choice.next_chapter}
#         )
#         if not created:
#             progress.current_chapter = choice.next_chapter
#             progress.save()

#         serializer = ChapterSerializer(choice.next_chapter)
#         return Response(serializer.data)

#     def get(self, request, pk):
#         chapter = get_object_or_404(Chapter, pk=pk)
#         serializer = ChapterSerializer(chapter)
#         return Response(serializer.data)

# API View for creating a new story
class CreateStoryView(APIView):
    @method_decorator(login_required)
    def post(self, request):
        serializer = StorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# API View for retrieving user progress
# class UserProgressView(APIView):
#     @method_decorator(login_required)
#     def get(self, request, user_id):
#         user = get_object_or_404(User, pk=user_id)
#         progress = UserProgress.objects.filter(user=user)
#         serializer = UserProgressSerializer(progress, many=True)
#         return Response(serializer.data)
