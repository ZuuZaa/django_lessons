from django.shortcuts import render, redirect
from .models import Main
from news.models import News
from cat.models import Cat


# Create your views here.
def home(request):
    
    # site = Main.objects.filter(pk=2)

    # return render(request, 'front/home.html', {'site':site})

    site = Main.objects.get(pk=2)
    news = News.objects.all().order_by('-pk')
    cat = Cat.objects.all()

    return render(request, 'front/home.html', 
        {'site':site, 'news':news, 'cat':cat} )


def about(request):

    title = "My Web | About"
    return render(request, 'front/about.html', {'title':title})

def panel(request):

    title = "My Web | Admin"
    return render(request, 'back/panel.html', {'title':title})

