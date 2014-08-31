from django.shortcuts import render, redirect
from .models import Disk, Box
from django.contrib import auth
from django.contrib import messages
from django.http import HttpResponse
from .disk import save_db


def index(request):
    return render(request, 'index.html')


def browse(request):
    boxs = Box.objects.values('box_no', 'created_at')
    return render(request, 'browse.html', {'boxs': boxs})


def disk_names(request, disk):
    names = Disk.objects.filter(disk_no=disk)
    if names:
        return render(request, 'names.html', {'names': names})
    else:
        return HttpResponse("Ops Something wrong happend") #TODO 404


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('pass')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('/add')
        else:
            messages.error(request, 'Username/Password is not valid!')
            return redirect(request.path)
    else:
        #return redirect("/browse")
        return redirect('/add')


def logout(request):
    auth.logout(request)
    return redirect("/browse")


def add(request):
    if request.user.is_authenticated():
        if request.method == "POST":
            box = request.POST.get('box')
            disk = request.POST.get('disk')
            save_db(box, disk)
            return render(request, 'add.html', {'success': "Database Updated"})
        else:
            return render(request, 'add.html')
    else:
        return HttpResponse("U r not logged in")


def search(request):
    if request.method == 'POST':
        boxs = Box.objects.values('box_no', 'created_at')
        search_term = request.POST.get('search', models=(Box.objects.values('box_no'),))
        result = Disk.objects.search(search_term)
        return render(request, 'browse.html', {'search' : result, 'boxs': boxs})