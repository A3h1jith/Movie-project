from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import movieForm
from movieapp.models import  movie


# Create your views here.
def index(request):
    movielist=movie.objects.all()
    context={'movies':movielist}
    return render(request,'index.html',context)

def details(request,movie_id):
    movies=movie.objects.get(id=movie_id)
    return render(request,'details.html',{'movies':movies})

def add_movie(request):
    if request.method=="POST":
        name=request.POST.get('name')
        year=request.POST.get('year')
        genre=request.POST.get('genre')
        description=request.POST.get('description')
        image=request.FILES['image']
        movies=movie(name=name,year=year,genre=genre,description=description,image=image)
        movies.save()

    return render(request,'add.html')

def update(request,id):
    movies=movie.objects.get(id=id)
    form=movieForm(request.POST or None,request.FILES,instance=movies)
    if form.is_valid():
         form.save()
         return redirect('/')
    return render(request,'edit.html',{'movies':movies,'form':form})

def delete(request,id):
    if request.method=='POST':
        movies = movie.objects.get(id=id)
        movies.delete()
        return redirect('/')
    return render(request,'delete.html')
