from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def baza(request):
    films = Movie.objects.all
    return render(request, 'movie/baza.html', {'films': films})

def movie_detail(request, movie_id):
    film = Movie.objects.get(id=movie_id)
    return render(request, 'movie/movie_detail.html', {'film': film})

def movie_review(request):
    if not request.user.is_authenticated:
        return
    if request.method == 'POST':
        movie_id = request.POST['movie_id']
        MovieReview.objects.create(
            author=request.user,
            movie=Movie.objects.get(id=movie_id),
            text=request.POST.get("text")
        )
    return redirect('movie_detail', movie_id=movie_id)