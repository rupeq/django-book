from django.urls import path
from . import views
from .views import *

app_name = 'BooksAPI'

urlpatterns = [
    path("books/all/", views.BooksView.as_view()),
    path("books/<int:pk>/", views.BooksFullView.as_view()),
    path('books/create/', BooksCreateView.as_view()),
]
