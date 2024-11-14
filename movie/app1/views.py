from django.shortcuts import render, redirect
from app1.models import Movie

# Create your views here.

def home(request):
    k=Movie.objects.all()
    return render(request,'home.html',{'movie':k})

def addmovie(request):
    if (request.method == "POST"):
        t=request.POST['t']
        d=request.POST['d']
        y=request.POST['y']
        l=request.POST['l']
        i=request.FILES['i']

        b=Movie.objects.create(title=t,description=d,year=y,language=l,image=i)
        b.save()
        return redirect('app1:home')

    return render(request,'add.html')

def detail(request,p):
    k=Movie.objects.get(id=p)
    return render(request,'detail.html',{'movie':k})

def edit(request,p):
    k=Movie.objects.get(id=p)
    if(request.method=="POST"):
        k.title=request.POST['t']
        k.description=request.POST['d']
        k.year=request.POST['y']
        k.language=request.POST['l']
        if(request.FILES.get('i')==None):
            k.save()
        else:
            k.image=request.FILES.get('i')
        k.save()
        return redirect('app1:home')
    return render(request,'edit.html',{'movie':k})

def delete(request,p):
    k=Movie.objects.get(id=p)
    k.delete()
    return redirect('app1:home')

