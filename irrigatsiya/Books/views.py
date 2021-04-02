from django.shortcuts import render
from .models import Books
from django.views.generic.edit import FormView
from .forms import BooksCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

class BooksListView(ListView):
    model = Books
    template_name = 'books_list.html'

    # context_object_name = 'books'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = Books.objects.all()
        return context

class BooksCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView, FormView):
    model = Books
    template_name = 'books_add.html'
    form_class = BooksCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(Books, self).form_valid(form)
    def test_func(self):
        if self.request.user.profile.is_teacher:
            return True
        return False

class BooksDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView, FormView):
    model = Books
    template_name = 'books_confirmation.html'

    def test_func(self):
        book = self.get_object()
        if book.author == self.request.user:
            return True


class BooksUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView, FormView):
    model = Books
