from django.urls import path
from . import views


urlpatterns = [
    path('api/books/comments', views.comment_list, name='books'),
    path('api/books/comments/<int:id>', views.comment_for_book, name='books'),
]