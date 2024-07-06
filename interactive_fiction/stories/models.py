from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
  # Inherit from AbstractUser for built-in authentication functionalities

  # Add custom fields specific to your application (optional)
  # Example: favorite_genre = models.CharField(max_length=50, blank=True)

  def __str__(self):
    return self.username


class Story(models.Model):
  title = models.CharField(max_length=255)
  author = models.CharField(max_length=50)  # Replace with User model in future
  description = models.TextField()

  def __str__(self):
    return self.title

class Choice(models.Model):
  story = models.ForeignKey(Story, on_delete=models.CASCADE)  # Link choice to a story
  text = models.CharField(max_length=255)
  # Add a field for next_story or next_choice based on your narrative structure

  def __str__(self):
    return self.text[:20]  # Truncate long choice text for better display
