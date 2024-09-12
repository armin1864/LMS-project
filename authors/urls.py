from django.urls import path
from .views import authors_list, author_bio, author_books

urlpatterns = [
    path('', authors_list),
    path('<int:pk>/bio', author_bio),
    path('<int:pk>/books', author_books),
]
