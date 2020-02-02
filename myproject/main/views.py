from django.shortcuts import render, redirect
from .models import Main
from news.models import News
from cat.models import Cat
from subcat.models import SubCat
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(request):
    
    # site = Main.objects.filter(pk=2)

    # return render(request, 'front/home.html', {'site':site})

    site = Main.objects.get(pk=2)
    news = News.objects.all().order_by('-pk')
    cat = Cat.objects.all()
    subcat = SubCat.objects.all()
    lastnews = News.objects.all().order_by('-pk')[:4]

    return render(request, 'front/home.html', 
        {'site':site, 'news':news, 'cat':cat, 'subcat':subcat, 'lastnews':lastnews} )



def about(request):

    title = "My Web | About"
 
    return render(request, 'front/about.html', {'title':title})


def panel(request):

    if not request.user.is_authenticated:
        return redirect('mylogin')

    title = "My Web | Admin"
    return render(request, 'back/panel.html', {'title':title})


def mylogin(request):

    if request.method == 'POST':

        uname = request.POST.get('username')
        upwd = request.POST.get('pwd')

        if uname != "" and upwd != "":

            user = authenticate(username = uname)

            print('-------------', uname)
            print('-------------', user)

            if user != None:

                login(request, user)
                print('------------- login')

                return redirect("panel")

            

    return render(request, 'front/login.html')

