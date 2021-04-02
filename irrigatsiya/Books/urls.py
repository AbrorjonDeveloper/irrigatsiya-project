from django.urls import path

from .views import BooksListView, BooksCreateView, BooksUpdateView,  BooksDeleteView


urlpatterns = [
    path('', BooksListView.as_view(), name="books"),
    path('new/', BooksCreateView.as_view(), name="book_add"),
    path('<slug:slug>/delete/', BooksDeleteView.as_view(), name="book_remove"),
    path('<slug:slug>/update/', BooksUpdateView.as_view(), name="book_update"),
]
