from django.shortcuts import render, redirect
from .models import Cat

def cat_list(request):

    cat = Cat.objects.all()

    return render(request, 'back/category.html', {'cat':cat})


def cat_add(request):


    if request.method == "POST":
                
        title = request.POST.get('cattitle').title()

        if title == "":

            error = "All fields are required"
            return render(request, 'back/error.html', {'error': error})
    

        if len(Cat.objects.filter(name=title)) !=0:

            error = "The Category name used before"
            return render(request, 'back/error.html', {'error': error}) 
                                              
        b = Cat(name=title)
        b.save()

        return redirect('cat_list')      


    return render(request, 'back/cat_add.html')

