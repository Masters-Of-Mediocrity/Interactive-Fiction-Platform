from django.contrib import admin
from .models import User, Story, Choice  # Replace with your model names

# Register your models here
admin.site.register(User)
admin.site.register(Story)
admin.site.register(Choice)