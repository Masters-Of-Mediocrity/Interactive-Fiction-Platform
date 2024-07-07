from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from .models import User, Story, StoryProgress  # Replace with your model names


def login_user(request):
  # Handle login form submission and user authentication logic
  # ...
  return render(request, 'login.html')  # Redirect to login template

def logout_user(request):
  logout(request)
  return redirect('home')  # Redirect to homepage after logout

def story_list(request):
  stories = Story.objects.all()
  return render(request, 'story_list.html', {'stories': stories})

def story_detail(request, story_id):
  story = get_object_or_404(Story, pk=story_id)
  return render(request, 'story_detail.html', {'story': story})

def user_story_progress(request):
  if not request.user.is_authenticated:
    return redirect('login')  # Redirect to login if not authenticated
  user = User.objects.get(pk=request.user.pk)
  progress_data = StoryProgress.objects.filter(user=user)  # Get user's progress data
  context = {'user': user, 'progress_data': progress_data}
  return render(request, 'user_story_progress.html', context)