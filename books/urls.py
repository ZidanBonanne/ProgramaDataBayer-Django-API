from books import views
from django.urls import path

urlpatterns = [
    path('books',views.BooksList.as_view()),
    path("books/<str:pk>",views.BooksDetail.as_view())
]