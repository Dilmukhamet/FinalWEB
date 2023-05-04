from django.urls import path
from . import views

urlpatterns = [
    path('api/genres/', views.create_genre, name='books'),
    path('api/genres/<int:pk>', views.genre_by_id, name='books'),
    path('api/genres/all', views.genre_list_view, name='books'),
    path('api/books', views.book_list, name='books'),
    path('api/books/all', views.book_list_view.as_view(), name='books'),
    path('api/books/<int:pk>', views.book_by_id.as_view(), name='books'),
    #path('api/books/<int:pk>', views.bookById.as_view(), name='books'),
    path('api/books/genres/<int:id>', views.books_by_genre, name='books'),
]