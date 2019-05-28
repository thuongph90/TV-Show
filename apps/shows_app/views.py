from django.shortcuts import render, redirect
from .models import shows
from django.contrib import messages
def shownew(request):
    # print('------**---')
    # print(request.POST)
    return render(request,'shows/new.html')
    

def showall(request):
    context={
        "allshow":shows.objects.all()
    }
    return render(request,"shows/index.html", context)

def showcreate(request):
    errors = shows.objects.basic_validator(request.POST)
    if len(errors)>0: 
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('/shows/new')
    else:
        show = shows.objects.create(title=request.POST['title'],network=request.POST['network'],released_date=request.POST['released_date'], description=request.POST['description'])
        # print('-------(((')
        # print(show.id)
        return redirect('/shows/'+str(show.id))
    

def showeach(request, id):
    context={
        "eachshow": shows.objects.get(id=id)
    }
    return render(request,"shows/showid.html", context)

def showedit(request,id):
    context={
        "eachshow": shows.objects.get(id=id)
    }
    return render(request,'shows/showedit.html',context)

def editdetail(request):
    c=shows.objects.get(id=request.POST['id_hidden'])
    c.title=request.POST['title']
    c.network=request.POST['network']
    c.released_date=request.POST['released_date']
    c.description=request.POST['description']
    c.save()
    return redirect('/shows/'+str(c.id))

def showdelete(request,id):
    show=shows.objects.get(id=id)
    show.delete()
    return redirect('/shows')
