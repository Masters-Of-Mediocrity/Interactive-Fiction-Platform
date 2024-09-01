from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    # avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return f"Profile of {self.user.username}"

class Story(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Chapter(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='chapters')
    title = models.CharField(max_length=255)
    content = models.TextField()
    order = models.IntegerField()

    def __str__(self):
        return f"{self.story.title} - Chapter {self.order}: {self.title}"

class Choice(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='choices')
    description = models.CharField(max_length=255)
    next_chapter = models.ForeignKey(Chapter, on_delete=models.SET_NULL, null=True, blank=True, related_name='previous_choices')

    def __str__(self):
        return f"Choice: {self.description} (Next: {self.next_chapter})"

class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    current_chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    progress = models.JSONField(default=dict)  # Stores choices made and paths taken

    def __str__(self):
        return f"{self.user.username}'s progress in {self.story.title}"
