from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
  # Inherit from AbstractUser for built-in authentication functionalities

  # Add custom fields specific to your application (optional)
  # favorite_genre = models.CharField(max_length=50, blank=True)
  # avatar = 

  def __str__(self):
    return self.username


class Story(models.Model):
  title = models.CharField(max_length=255)
  # author = models.CharField(max_length=50)  # Replace with User model in future
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  description = models.TextField()

  def __str__(self):
    return self.title

class Choice(models.Model):
  story = models.ForeignKey(Story, on_delete=models.CASCADE)  # Link choice to a story
  text = models.CharField(max_length=255)
  # Add a field for next_story or next_choice based on your narrative structure

  def __str__(self):
    return self.text[:20]  # Truncate long choice text for better display

class StoryProgress(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to User model
  story = models.ForeignKey(Story, on_delete=models.CASCADE)  # Link to Story model
  current_choice = models.ForeignKey(Choice, on_delete=models.SET_NULL, null=True, blank=True)  # Track current choice within story (optional)
  completed = models.BooleanField(default=False)  # Flag to indicate if story is completed

  class Meta:
    unique_together = (('user', 'story'),)  # Ensure unique progress record per user/story

  def __str__(self):
    return f"{self.user.username} - {self.story.title} (Completed: {self.completed})"

