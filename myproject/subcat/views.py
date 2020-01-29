from django.shortcuts import render, redirect
from .models import SubCat
from cat.models import Cat

def subcat_list(request):

    subcat = SubCat.objects.all()

    return render(request, 'back/subcategory.html', {'subcat':subcat})


def subcat_add(request):

    cat = Cat.objects.all()


    if request.method == "POST":
                
        subtitle = request.POST.get('subcattitle').title()
        catid = request.POST.get('category')
        category = Cat.objects.get(pk=catid).name
    

        if subtitle == "":

            error = "All fields are required"
            return render(request, 'back/error.html', {'error': error})
    

        if len(SubCat.objects.filter(name = subtitle)) !=0:

            error = "The Category name used before"
            return render(request, 'back/error.html', {'error': error}) 

        
        b = SubCat(name = subtitle, catname = category, catid=catid)
        b.save()

        return redirect('subcat_list')      
        
        

    return render(request, 'back/subcat_add.html', {'cat':cat})

