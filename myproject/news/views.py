from django.shortcuts import render, redirect
from main.models import Main
from .models import News
from django.core.files.storage import FileSystemStorage

# Create your views here.
def news_detail(request, word):
    
    # site = Main.objects.filter(pk=2)

    # return render(request, 'front/home.html', {'site':site})

    site = Main.objects.get(pk=2)
    news = News.objects.filter(name=word)

    return render(request, 'front/news_detail.html', 
        {'site':site, 'news':news} )

def news_list(request):

        news = News.objects.all()

        return render(request, 'back/news_list.html', {'news':news})

def news_add(request):

        if request.method == "POST":
                
                title = request.POST.get('newstitle')
                category = request.POST.get('newscat')
                short_txt = request.POST.get('shorttext')
                body_txt = request.POST.get('bodytext')
                picname =request.POST.get('picname')

                if title == "" or short_txt == "" or body_txt == "" or category == "":

                        error = "All fields are required"
                        return render(request, 'back/error.html', {'error': error})
                
                try: 
                                
                        myfile = request.FILES['myfile']
                        fs = FileSystemStorage()
                        filename = fs.save(myfile.name, myfile)
                        url = fs.url(filename)
                        b = News(name=title, 
                                category=category,
                                catid=0, 
                                short_txt=short_txt, 
                                body_txt=body_txt, date="2020", 
                                picname = picname,
                                picurl=url, 
                                writer="admin", 
                                view =0,)
                        b.save()

                        return redirect('news_list')
                
                except:
                        error = "Please load image."
                        return render(request, 'back/error.html', {'error': error}) 
        

        return render(request, 'back/news_add.html')