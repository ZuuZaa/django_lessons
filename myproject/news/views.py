from django.shortcuts import render, redirect
from main.models import Main
from .models import News
from django.core.files.storage import FileSystemStorage
import datetime
from subcat.models import SubCat




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

        now = datetime.datetime.now()

        year = now.year
        month = now.month
        day = now.day
        hour = now.hour
        minute = now.minute

        if len(str(day)) == 1:
                day = "0" + str(day)

        if len(str(month)) == 1:
                month = "0" + str(month)

        today = str(day) + '.' + str(month) + '.' + str(year) + '.'
        time = str(hour) + ':' + str(minute)

        cat = SubCat.objects.all()

        if request.method == "POST":
                
                title = request.POST.get('newstitle')
                short_txt = request.POST.get('shorttext')
                body_txt = request.POST.get('bodytext')
                picname = request.POST.get('picname')
                catid = request.POST.get('newscat')
                catname = SubCat.objects.get(pk=catid).name


                if title == "" or short_txt == "" or body_txt == "":

                        error = "All fields are required"
                        return render(request, 'back/error.html', {'error': error})
                
                try: 
                                
                        myfile = request.FILES['myfile']
                        fs = FileSystemStorage()
                        filename = fs.save(myfile.name, myfile)
                        url = fs.url(filename)

                        if str(myfile.content_type).startswith('image'):

                                if myfile.size < 5000000:


                                        b = News(name=title, 
                                                category= catname,
                                                date = today,
                                                time =time,
                                                catid=catid, 
                                                short_txt=short_txt, 
                                                body_txt=body_txt,
                                                picname = picname,
                                                picurl=url, 
                                                writer="admin", 
                                                view =0,)
                                        b.save()

                                        return redirect('news_list')

                                else:

                                        fs = FileSystemStorage()
                                        fs.delete(filename)
                                        error = "Your file is bigger than 5mb"
                                        return render(request, 'back/error.html', {'error': error})   
                        else:
                                error = "Your file not supported"
                                return render(request, 'back/error.html', {'error': error})  
                        
                except:
                        error = "Please load image."
                        return render(request, 'back/error.html', {'error': error}) 
        

        return render(request, 'back/news_add.html', {'cat':cat})


def news_delete(request, pk):

        try:

                b = News.objects.get(pk=pk)
                fs = FileSystemStorage()
                fs.delete(b.picname)
                b.delete()

        except:
                error = "something wrong"
                return render(request, 'back/error.html', {'error': error}) 


        return redirect('news_list')

def news_edit(request, pk):


        if len(News.objects.filter(pk=pk)) == 0:
                error = "News not found"
                return render(request, 'back/error.html', {'error': error}) 

        news = News.objects.get(pk=pk)
        cat = SubCat.objects.all()

        
        if request.method == "POST":
                
                title = request.POST.get('newstitle')
                short_txt = request.POST.get('shorttext')
                body_txt = request.POST.get('bodytext')
                picname = request.POST.get('picname')
                catid = request.POST.get('newscat')
                catname = SubCat.objects.get(pk=catid).name


                if title == "" or short_txt == "" or body_txt == "":

                        error = "All fields are required"
                        return render(request, 'back/error.html', {'error': error})
                
                try: 
                                
                        myfile = request.FILES['myfile']
                        fs = FileSystemStorage()
                        filename = fs.save(myfile.name, myfile)
                        url = fs.url(filename)

                        if str(myfile.content_type).startswith('image'):

                                if myfile.size < 5000000:

                                        b = News.objects.get(pk=pk)

                                        fss = FileSystemStorage()
                                        fss.delete(b.picname)

                                        b.name = title
                                        b.category = catname
                                        b.short_txt=short_txt
                                        b.body_txt=body_txt
                                        b.picname = picname
                                        b.picurl= url
                                       
                                        b.save()

                                        return redirect('news_list')

                                else:

                                        fs = FileSystemStorage()
                                        fs.delete(filename)
                                        error = "Your file is bigger than 5mb"
                                        return render(request, 'back/error.html', {'error': error})   
                        else:
                                error = "Your file not supported"
                                return render(request, 'back/error.html', {'error': error})  
                        
                except:
                        b = News.objects.get(pk=pk)


                        b.name = title
                        b.category = catname
                        b.short_txt=short_txt
                        b.body_txt=body_txt
                                       
                        b.save()

                        return redirect('news_list') 





        return render(request, 'back/news_edit.html', {'news': news, 'cat': cat})       