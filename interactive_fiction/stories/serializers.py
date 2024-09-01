from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Story, Chapter, Choice, UserProgress

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

# Profile Serializer
class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'user', 'bio']

# Choice Serializer
class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'chapter', 'description', 'next_chapter']

# Chapter Serializer
class ChapterSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)  # Nested relationship to include choices

    class Meta:
        model = Chapter
        fields = ['id', 'story', 'title', 'content', 'order', 'choices']

# Story Serializer
class StorySerializer(serializers.ModelSerializer):
    chapters = ChapterSerializer(many=True, read_only=True)  # Nested relationship to include chapters
    author = UserSerializer(read_only=True)  # Include author details

    class Meta:
        model = Story
        fields = ['id', 'author', 'title', 'description', 'created_at', 'updated_at', 'chapters']

# User Progress Serializer
class UserProgressSerializer(serializers.ModelSerializer):
    story = StorySerializer(read_only=True)
    current_chapter = ChapterSerializer(read_only=True)
    user = UserSerializer(read_only=True)  # Include user details

    class Meta:
        model = UserProgress
        fields = ['id', 'user', 'story', 'current_chapter', 'progress']
