from django.contrib import admin
from .models import Profile, Story, Chapter, Choice, UserProgress  # Replace with your model names

# Register your models here
admin.site.register(Profile)
admin.site.register(Story)
admin.site.register(Chapter)
admin.site.register(Choice)
admin.site.register(UserProgress)