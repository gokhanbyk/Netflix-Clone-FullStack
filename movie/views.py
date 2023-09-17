from django.shortcuts import render, redirect
from user.models import *
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return redirect('profile_page')
    return render(request,'index.html')

@login_required(login_url="/login/")
def movie(request, id):
    profile = Profile.objects.get(pk = id)
    profiller = request.user.profile_set.all()

    if 'q' in request.GET and request.GET.get('q'):
        q = request.GET.get('q')
        turler = Genre.objects.filter(title__contains = q)
        filmler = Movie.objects.filter(title__contains = q) or Movie.objects.filter(genre__in=turler)
        return render(request, 'movie.html', {
            'profile': profile,
            'profiller': profiller,
            'id': id,
            'filmler': filmler,
        })

   
    filmler = Movie.objects.all()

    return render(request, 'movie.html', {
        'profile': profile,
        'profiller': profiller,
        'id': id,
        'filmler': filmler,
    })

@login_required(login_url="/login/")
def movie_detail(request, slug):
    film = Movie.objects.get(slug = slug)

    return render(request, 'movie_detail.html', {
        'film': film
    })
