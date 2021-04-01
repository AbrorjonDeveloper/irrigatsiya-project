from django.shortcuts import render
from .models import Articles
from django.views.generic import (
    ListView, 
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

class ArticleListView(ListView):
    model = Articles
    template_name = 'article_list.html'
    ordering = ['-up_date', '-pub_date', ]
    context_object_name = 'articles'

class ArticleCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Articles
    template_name = 'article_create.html'
    fields = ['name', 'category', 'article', 'link']
    def form_valid(self, form):
        form.instance.author = self.request.user 
        messages.success(self.request, f'Article added successfully!')
        return super().form_valid(form)
        
    
    def test_func(self):
        if self.request.user.is_staff:
            return True

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Articles
    template_name = 'article_update.html'
    fields = ['name', 'category', 'article', 'link']
    def test_func(self):
        article = self.get_object()
        if article.author == self.request.user:
            return True
        return False
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Article has been updated!')
        return super().form_valid(form)

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Articles
    template_name = 'article_delete.html'

    def test_func(self):
        article = self.get_object()
        if article.author == self.request.user:
            return True
        return False

