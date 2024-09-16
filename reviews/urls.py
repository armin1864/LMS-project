from django.urls import path
from .views import submit_review, see_reviews


urlpatterns = [
    path('submit/', submit_review, name='submit_review'),
    path('<int:pk>/', see_reviews, name='see_reviews')
]
