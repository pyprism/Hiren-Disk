from django.shortcuts import render, redirect
from .models import Disk, Box
from django.contrib import auth
# Create your views here.


def index(request):
    return render(request, 'index.html', {'browse': "browse", "add": "x"})


def browse(request):
    no = Box.objects.values('disk_no', 'created_at')
    return render(request, 'browse.html', {'no' : no})


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('pass')
        #print(email, password)
        user = auth.authenticate(username=username, password=password)
        print(user)
        if user:
            return redirect('/add')
    else:
        return redirect('/browse')