from django.contrib import admin
from django.urls import path, include

from .views import (
    ArticleListView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
)

urlpatterns = [
    path('list/', ArticleListView.as_view(), name="articles"),
    path('new/', ArticleCreateView.as_view(), name="article_create"),
    path('<slug:slug>/update/', ArticleUpdateView.as_view(), name="article_update"),
]