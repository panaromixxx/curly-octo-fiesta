from django.urls import path
from movie.views import *

urlpatterns = [
    path('', baza, name="baza"),
    path('movie/<int:movie_id>/', movie_detail, name="movie_detail"),
    path('movie_review/', movie_review, name='movie_review'),
]
