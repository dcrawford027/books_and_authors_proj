from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_book', views.addBook),
    path('book_details/<int:book_id>', views.bookDetails),
    path('book_details/<int:book_id>/append_author', views.appendAuthor)
]