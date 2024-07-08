from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Story, Chapter, Choice, UserProgress
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView

class StoryListView(ListView):
    model = Story
    template_name = 'stories/story_list.html'
    context_object_name = 'stories'

class StoryDetailView(DetailView):
    model = Story
    template_name = 'stories/story_detail.html'
    context_object_name = 'story'

class ChapterDetailView(DetailView):
    model = Chapter
    template_name = 'stories/chapter_detail.html'
    context_object_name = 'chapter'

    def post(self, request, *args, **kwargs):
        chapter = self.get_object()
        choice_id = request.POST.get('choice_id')
        choice = get_object_or_404(Choice, id=choice_id)
        
        # Update user progress
        progress, created = UserProgress.objects.get_or_create(
            user=request.user, story=chapter.story,
            defaults={'current_chapter': choice.next_chapter}
        )
        if not created:
            progress.current_chapter = choice.next_chapter
            progress.save()

        return redirect('chapter_detail', pk=choice.next_chapter.pk)

class CreateStoryView(CreateView):
    model = Story
    fields = ['title', 'description']
    template_name = 'stories/story_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UserProgressView(DetailView):
    model = User
    template_name = 'stories/user_progress.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['progress'] = UserProgress.objects.filter(user=self.object)
        return context
