from django.shortcuts import render, redirect
from .models import Disk, Box
from django.contrib import auth
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'index.html', {'browse': "browse", "add": "x"})


def browse(request):
    no = Box.objects.values('disk_no', 'created_at')
    return render(request, 'browse.html', {'no': no})


def disk_names(request, disk):
    names = Disk.objects.filter(box_no=disk)
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
        return render(request, 'add.html')
    else:
        return HttpResponse("U r not logged in")