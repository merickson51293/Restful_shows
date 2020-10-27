from django.shortcuts import render, redirect
from restful_app.models import *

def index(request):
    return render(request, "index.html")

def shows(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, "shows.html", context)

def show_desc(request, show_id):
    one_show = Show.objects.get(id=show_id)
    context = {
        'show': one_show
    }
    return render(request, "show_desc.html", context)

def new_show(request):
    if request.method=='POST':
        new_show = Show.objects.create(
        title=request.POST['title'],
        network=request.POST['network'],
        release_date=request.POST['release_date'],
        desc=request.POST['desc']
        )
        return redirect(f'/shows_desc/{new_show.id}')
    return render(request, "new_show.html")


def edit_show(request, show_id):
    one_show = Show.objects.get(id=show_id)
    context = {
        'show': one_show
    }
    return render(request, "edit_show.html", context)

def show_delete(request, show_id):
    to_delete = Show.objects.get(id=show_id)
    to_delete.delete()
    return redirect('/shows')