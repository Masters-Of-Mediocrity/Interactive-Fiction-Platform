from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .models import User, StoryProgress  # Replace with your model names


def login_user(request):
  # Handle login form submission and user authentication logic
  # ...
  return render(request, 'login.html')  # Redirect to login template

def logout_user(request):
  logout(request)
  return redirect('home')  # Redirect to homepage after logout


def user_story_progress(request):
  if not request.user.is_authenticated:
    return redirect('login')  # Redirect to login if not authenticated
  user = User.objects.get(pk=request.user.pk)
  progress_data = StoryProgress.objects.filter(user=user)  # Get user's progress data
  context = {'user': user, 'progress_data': progress_data}
  return render(request, 'user_story_progress.html', context)